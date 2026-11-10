
"""Production application entry for Company AI OS Workflow."""

from core.core import process
from employees.assignment import assign_employee
from workflow.core_runner import CoreTaskRunner
from workflow.engine import WorkflowEngine
from workflow.task_store import TaskStore


class WorkflowApplication:
    """Connect CORE, AI Employees, and Workflow for production use."""

    def __init__(
        self,
        db_path="data/tasks.db",
        max_retries=3,
        validate_answers=True,
        validation_options=None,
    ):
        self.store = TaskStore(db_path)
        self.engine = WorkflowEngine(
            self.store,
            max_retries=max_retries,
        )
        self.runner = CoreTaskRunner(
            process,
            include_previous_result=True,
            validate_answers=validate_answers,
            **(validation_options or {}),
        )

    def run(self, task_definitions):
        """Assign employees and execute a sequential Workflow."""
        assigned_tasks = []

        for definition in task_definitions:
            employee_id = (definition.get("input_data") or {}).get(
                "employee_id"
            )

            if not employee_id:
                raise ValueError(
                    f"Task '{definition.get('name', '')}' "
                    "requires input_data['employee_id']."
                )

            assigned_tasks.append(
                assign_employee(definition, employee_id)
            )

        return self.engine.run(
            assigned_tasks,
            self.runner,
        )


def run_workflow(
    task_definitions,
    db_path="data/tasks.db",
    max_retries=3,
    validate_answers=True,
    validation_options=None,
):
    """Convenience function for running a production Workflow."""
    application = WorkflowApplication(
        db_path=db_path,
        max_retries=max_retries,
        validate_answers=validate_answers,
        validation_options=validation_options,
    )
    return application.run(task_definitions)
