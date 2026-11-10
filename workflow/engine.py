
"""Sequential Workflow Engine with persistent resume support."""


class WorkflowEngine:
    def __init__(self, task_store, max_retries=3):
        if not isinstance(max_retries, int) or isinstance(max_retries, bool):
            raise TypeError("max_retries must be an integer")
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")

        self.task_store = task_store
        self.max_retries = max_retries

    def _run_task(self, task, runner, previous_result):
        """Execute a running Task with retries."""
        last_error = None

        for attempt in range(self.max_retries + 1):
            try:
                result = runner(task, previous_result)
                return self.task_store.transition(
                    task["task_id"],
                    "completed",
                    result=result,
                )
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                print(
                    f"[WORKFLOW RETRY] Task='{task['name']}', "
                    f"attempt={attempt + 1}/{self.max_retries + 1}, "
                    f"error={last_error}"
                )

        return self.task_store.transition(
            task["task_id"],
            "paused",
            error=last_error,
        )

    def run(self, task_definitions, runner):
        """Create and run a persistent Workflow sequentially."""
        if not callable(runner):
            raise TypeError("runner must be callable")

        definitions = list(task_definitions)

        if not definitions:
            return {
                "status": "completed",
                "tasks": [],
                "final_result": None,
            }

        # Validate all definitions before creating database records.
        for definition in definitions:
            if not isinstance(definition, dict):
                raise TypeError("Each task definition must be a dictionary")
            if not isinstance(definition.get("name"), str):
                raise ValueError("Each task definition needs a non-empty name")
            if not definition["name"].strip():
                raise ValueError("Each task definition needs a non-empty name")
            if not isinstance(definition.get("input_data", {}), dict):
                raise TypeError("input_data must be a dictionary")
            if not isinstance(definition.get("description", ""), str):
                raise TypeError("description must be a string")

        # Create every Task first so the complete Workflow is recoverable.
        tasks = [
            self.task_store.create_task(
                name=definition["name"],
                description=definition.get("description", ""),
                input_data=definition.get("input_data", {}),
            )
            for definition in definitions
        ]
        task_ids = [task["task_id"] for task in tasks]
        workflow = self.task_store.create_workflow(task_ids)

        self.task_store.update_workflow(
            workflow["workflow_id"],
            status="running",
            current_task_index=0,
        )

        task_records = []
        previous_result = None

        for index, task in enumerate(tasks):
            task = self.task_store.transition(task["task_id"], "running")
            task = self._run_task(task, runner, previous_result)
            task_records.append(task)

            if task["status"] == "paused":
                self.task_store.update_workflow(
                    workflow["workflow_id"],
                    status="paused",
                    current_task_index=index,
                )
                return {
                    "status": "paused",
                    "workflow_id": workflow["workflow_id"],
                    "tasks": task_records,
                    "paused_task_id": task["task_id"],
                    "error": task["error"],
                    "final_result": previous_result,
                }

            previous_result = task["result"]
            self.task_store.update_workflow(
                workflow["workflow_id"],
                status="running",
                current_task_index=index + 1,
            )

        self.task_store.update_workflow(
            workflow["workflow_id"],
            status="completed",
            current_task_index=len(tasks),
        )

        return {
            "status": "completed",
            "workflow_id": workflow["workflow_id"],
            "tasks": task_records,
            "final_result": previous_result,
        }

    def resume_task(
        self, task_id, runner, decision="retry", previous_result=None
    ):
        """Resume one paused Task after a human decision."""
        if not callable(runner):
            raise TypeError("runner must be callable")

        task = self.task_store.get_task(task_id)
        if task is None:
            raise KeyError(f"Task not found: {task_id}")

        if task["status"] != "paused":
            raise ValueError(
                f"Only paused Tasks can be resumed: {task['status']}"
            )

        if decision == "cancel":
            return self.task_store.transition(
                task_id,
                "failed",
                error="人間の判断によりTaskを中止しました。",
            )

        if decision != "retry":
            raise ValueError("decision must be 'retry' or 'cancel'")

        task = self.task_store.transition(task_id, "running")
        last_error = None

        for attempt in range(self.max_retries + 1):
            try:
                result = runner(task, previous_result)
                return self.task_store.transition(
                    task_id,
                    "completed",
                    result=result,
                )
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                print(
                    f"[WORKFLOW RESUME RETRY] Task='{task['name']}', "
                    f"attempt={attempt + 1}/{self.max_retries + 1}, "
                    f"error={last_error}"
                )

        return self.task_store.transition(
            task_id,
            "paused",
            error=last_error,
        )

    def resume_workflow(self, workflow_id, runner, decision="retry"):
        """Resume a paused Workflow, skipping already completed Tasks."""
        if not callable(runner):
            raise TypeError("runner must be callable")

        workflow = self.task_store.get_workflow(workflow_id)
        if workflow is None:
            raise KeyError(f"Workflow not found: {workflow_id}")

        if workflow["status"] != "paused":
            raise ValueError(
                f"Only paused Workflows can be resumed: "
                f"{workflow['status']}"
            )

        if decision not in ("retry", "cancel"):
            raise ValueError("decision must be 'retry' or 'cancel'")

        task_ids = workflow["task_ids"]
        tasks = [self.task_store.get_task(task_id) for task_id in task_ids]

        if any(task is None for task in tasks):
            raise ValueError("Workflow contains an unknown Task ID.")

        index = workflow["current_task_index"]

        if not 0 <= index < len(tasks):
            raise ValueError("Workflow resume position is invalid.")

        # Recover the most recent completed result before the paused Task.
        previous_result = None
        for task in tasks[:index]:
            if task["status"] != "completed":
                raise ValueError(
                    "A preceding Task is not completed; "
                    "cannot safely resume this Workflow."
                )
            previous_result = task["result"]

        paused_task = tasks[index]
        if paused_task["status"] != "paused":
            raise ValueError(
                "The Workflow's current Task is not paused."
            )

        if decision == "cancel":
            self.task_store.transition(
                paused_task["task_id"],
                "failed",
                error="人間の判断によりWorkflowを中止しました。",
            )
            self.task_store.update_workflow(
                workflow_id,
                status="failed",
                current_task_index=index,
            )
            return {
                "status": "failed",
                "workflow_id": workflow_id,
                "tasks": [
                    self.task_store.get_task(task_id)
                    for task_id in task_ids
                ],
                "final_result": previous_result,
            }

        task = self.resume_task(
            paused_task["task_id"],
            runner,
            decision="retry",
            previous_result=previous_result,
        )

        if task["status"] == "paused":
            self.task_store.update_workflow(
                workflow_id,
                status="paused",
                current_task_index=index,
            )
            return {
                "status": "paused",
                "workflow_id": workflow_id,
                "tasks": [
                    self.task_store.get_task(task_id)
                    for task_id in task_ids
                ],
                "paused_task_id": task["task_id"],
                "error": task["error"],
                "final_result": previous_result,
            }

        previous_result = task["result"]
        self.task_store.update_workflow(
            workflow_id,
            status="running",
            current_task_index=index + 1,
        )

        # Continue with pending Tasks, without repeating completed Tasks.
        for next_index in range(index + 1, len(task_ids)):
            task = self.task_store.get_task(task_ids[next_index])

            if task["status"] == "completed":
                previous_result = task["result"]
                self.task_store.update_workflow(
                    workflow_id,
                    status="running",
                    current_task_index=next_index + 1,
                )
                continue

            if task["status"] != "pending":
                raise ValueError(
                    f"Cannot continue Workflow: Task '{task['name']}' "
                    f"has status '{task['status']}'."
                )

            task = self.task_store.transition(
                task["task_id"], "running"
            )
            task = self._run_task(task, runner, previous_result)

            if task["status"] == "paused":
                self.task_store.update_workflow(
                    workflow_id,
                    status="paused",
                    current_task_index=next_index,
                )
                return {
                    "status": "paused",
                    "workflow_id": workflow_id,
                    "tasks": [
                        self.task_store.get_task(task_id)
                        for task_id in task_ids
                    ],
                    "paused_task_id": task["task_id"],
                    "error": task["error"],
                    "final_result": previous_result,
                }

            previous_result = task["result"]
            self.task_store.update_workflow(
                workflow_id,
                status="running",
                current_task_index=next_index + 1,
            )

        self.task_store.update_workflow(
            workflow_id,
            status="completed",
            current_task_index=len(task_ids),
        )

        return {
            "status": "completed",
            "workflow_id": workflow_id,
            "tasks": [
                self.task_store.get_task(task_id)
                for task_id in task_ids
            ],
            "final_result": previous_result,
        }

    def _sync_workflow_state(self, workflow_id, task_ids):
        """Synchronize Workflow status and resume position from Task records."""
        tasks = [self.task_store.get_task(task_id) for task_id in task_ids]

        if any(task is None for task in tasks):
            raise ValueError("Workflow contains an unknown Task ID.")

        paused_index = next(
            (
                index
                for index, task in enumerate(tasks)
                if task["status"] == "paused"
            ),
            None,
        )

        failed_index = next(
            (
                index
                for index, task in enumerate(tasks)
                if task["status"] == "failed"
            ),
            None,
        )

        first_incomplete = next(
            (
                index
                for index, task in enumerate(tasks)
                if task["status"] != "completed"
            ),
            len(tasks),
        )

        if paused_index is not None:
            status = "paused"
            current_index = paused_index
        elif failed_index is not None:
            status = "failed"
            current_index = failed_index
        elif first_incomplete == len(tasks):
            status = "completed"
            current_index = len(tasks)
        else:
            status = "running"
            current_index = first_incomplete

        return self.task_store.update_workflow(
            workflow_id,
            status=status,
            task_ids=task_ids,
            current_task_index=current_index,
        )
