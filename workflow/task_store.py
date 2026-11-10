"""Persistent task records for Company AI OS.

Step 1 only: task data and status management.
This module does not execute tasks or call the LLM.
"""

import json
from contextlib import closing
import os
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path


VALID_STATUSES = {
    "pending",
    "running",
    "paused",
    "completed",
    "failed",
}

ALLOWED_TRANSITIONS = {
    "pending": {"running", "failed"},
    "running": {"paused", "completed", "failed"},
    "paused": {"running", "failed"},
    "completed": set(),
    "failed": set(),
}


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class TaskStore:
    """Create and manage persistent Task records in SQLite."""

    def __init__(self, db_path="data/tasks.db"):
        self.db_path = str(db_path)
        parent = Path(self.db_path).parent
        if self.db_path != ":memory:" and str(parent) not in ("", "."):
            parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self):
        with closing(self._connect()) as conn, conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL DEFAULT '',
                    status TEXT NOT NULL,
                    input_data TEXT NOT NULL DEFAULT '{}',
                    result TEXT,
                    error TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )

            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS workflows (
                    workflow_id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    task_ids TEXT NOT NULL DEFAULT '[]',
                    current_task_index INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )

    @staticmethod
    def _row_to_dict(row):
        if row is None:
            return None
        task = dict(row)
        task["input_data"] = json.loads(task["input_data"])
        task["result"] = (
            json.loads(task["result"]) if task["result"] is not None else None
        )
        return task

    def create_task(self, name, description="", input_data=None):
        """Create a Task in pending state and return its record."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Task name must be a non-empty string.")
        if input_data is not None and not isinstance(input_data, dict):
            raise TypeError("input_data must be a dictionary or None.")

        timestamp = _now()
        task_id = str(uuid.uuid4())
        serialized_input = json.dumps(
            input_data or {}, ensure_ascii=False
        )

        with closing(self._connect()) as conn, conn:
            conn.execute(
                """
                INSERT INTO tasks (
                    task_id, name, description, status, input_data,
                    result, error, created_at, updated_at
                )
                VALUES (?, ?, ?, 'pending', ?, NULL, NULL, ?, ?)
                """,
                (
                    task_id,
                    name.strip(),
                    description,
                    serialized_input,
                    timestamp,
                    timestamp,
                ),
            )

        return self.get_task(task_id)

    def get_task(self, task_id):
        with closing(self._connect()) as conn, conn:
            row = conn.execute(
                "SELECT * FROM tasks WHERE task_id = ?", (task_id,)
            ).fetchone()
        return self._row_to_dict(row)

    def list_tasks(self, status=None):
        if status is not None and status not in VALID_STATUSES:
            raise ValueError(f"Invalid Task status: {status}")

        with closing(self._connect()) as conn, conn:
            if status is None:
                rows = conn.execute(
                    "SELECT * FROM tasks ORDER BY created_at, task_id"
                ).fetchall()
            else:
                rows = conn.execute(
                    """
                    SELECT * FROM tasks
                    WHERE status = ?
                    ORDER BY created_at, task_id
                    """,
                    (status,),
                ).fetchall()

        return [self._row_to_dict(row) for row in rows]

    def transition(self, task_id, new_status, result=None, error=None):
        """Change status only when the transition is allowed."""
        if new_status not in VALID_STATUSES:
            raise ValueError(f"Invalid Task status: {new_status}")

        task = self.get_task(task_id)
        if task is None:
            raise KeyError(f"Task not found: {task_id}")

        old_status = task["status"]
        if new_status not in ALLOWED_TRANSITIONS[old_status]:
            raise ValueError(
                f"Invalid Task status transition: {old_status} -> {new_status}"
            )

        if new_status == "completed" and error:
            raise ValueError("A completed Task cannot have an error.")
        if new_status == "failed" and not error:
            error = "Task failed without a recorded error."

        serialized_result = (
            json.dumps(result, ensure_ascii=False)
            if result is not None
            else None
        )

        with closing(self._connect()) as conn, conn:
            conn.execute(
                """
                UPDATE tasks
                SET status = ?, result = ?, error = ?, updated_at = ?
                WHERE task_id = ?
                """,
                (
                    new_status,
                    serialized_result,
                    error,
                    _now(),
                    task_id,
                ),
            )

        return self.get_task(task_id)

    
    def create_workflow(self, task_ids=None):
        """Create a persistent Workflow record."""
        if task_ids is None:
            task_ids = []
        if not isinstance(task_ids, list):
            raise TypeError("task_ids must be a list")
        if not all(isinstance(task_id, str) for task_id in task_ids):
            raise TypeError("Each task_id must be a string")
        if len(task_ids) != len(set(task_ids)):
            raise ValueError("Duplicate Task IDs are not allowed")

        # すべてのTask IDが存在することを確認
        for task_id in task_ids:
            if self.get_task(task_id) is None:
                raise ValueError(f"Task not found: {task_id}")

        workflow_id = str(uuid.uuid4())
        timestamp = _now()

        with closing(self._connect()) as conn, conn:
            conn.execute(
                """
                INSERT INTO workflows (
                    workflow_id, status, task_ids,
                    current_task_index, created_at, updated_at
                )
                VALUES (?, 'pending', ?, 0, ?, ?)
                """,
                (
                    workflow_id,
                    json.dumps(task_ids, ensure_ascii=False),
                    timestamp,
                    timestamp,
                ),
            )

        return self.get_workflow(workflow_id)

    def get_workflow(self, workflow_id):
        """Retrieve a Workflow record by ID."""
        with closing(self._connect()) as conn, conn:
            row = conn.execute(
                "SELECT * FROM workflows WHERE workflow_id = ?",
                (workflow_id,),
            ).fetchone()

        if row is None:
            return None

        workflow = dict(row)
        workflow["task_ids"] = json.loads(workflow["task_ids"])
        return workflow

    def update_workflow(
        self,
        workflow_id,
        status=None,
        task_ids=None,
        current_task_index=None,
    ):
        """Update Workflow status, ordered tasks, or resume position."""
        workflow = self.get_workflow(workflow_id)
        if workflow is None:
            raise KeyError(f"Workflow not found: {workflow_id}")

        if status is not None and status not in VALID_STATUSES:
            raise ValueError(f"Invalid Workflow status: {status}")
        
        if task_ids is not None:
            if not isinstance(task_ids, list):
                raise TypeError("task_ids must be a list")
            if not all(isinstance(task_id, str) for task_id in task_ids):
                raise TypeError("Each task_id must be a string")
            if len(task_ids) != len(set(task_ids)):
                raise ValueError("Duplicate Task IDs are not allowed")

            # すべてのTask IDが存在することを確認
            for task_id in task_ids:
                if self.get_task(task_id) is None:
                    raise ValueError(f"Task not found: {task_id}")


        if current_task_index is not None:
            if (
                not isinstance(current_task_index, int)
                or isinstance(current_task_index, bool)
            ):
                raise TypeError("current_task_index must be an integer")
            if not 0 <= current_task_index <= len(
                task_ids if task_ids is not None else workflow["task_ids"]
            ):
                raise ValueError("current_task_index is out of range")

        new_status = status if status is not None else workflow["status"]
        new_task_ids = (
            json.dumps(task_ids, ensure_ascii=False)
            if task_ids is not None
            else json.dumps(workflow["task_ids"], ensure_ascii=False)
        )
        new_index = (
            current_task_index
            if current_task_index is not None
            else workflow["current_task_index"]
        )

        with closing(self._connect()) as conn, conn:
            conn.execute(
                """
                UPDATE workflows
                SET status = ?, task_ids = ?,
                    current_task_index = ?, updated_at = ?
                WHERE workflow_id = ?
                """,
                (
                    new_status,
                    new_task_ids,
                    new_index,
                    _now(),
                    workflow_id,
                ),
            )

        return self.get_workflow(workflow_id)

