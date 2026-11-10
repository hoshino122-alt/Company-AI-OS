
"""Task assignment helpers for Company AI OS."""

from employees.registry import get_employee


def assign_employee(task_definition, employee_id):
    """Return a Task definition assigned to an enabled employee."""
    if not isinstance(task_definition, dict):
        raise TypeError("task_definition must be a dictionary")

    if not isinstance(employee_id, str) or not employee_id.strip():
        raise ValueError("employee_id must be a non-empty string.")

    employee_id = employee_id.strip()
    employee = get_employee(employee_id)

    if employee is None:
        raise ValueError(f"Unknown employee_id: {employee_id}")

    if not employee["enabled"]:
        raise ValueError(f"Employee '{employee_id}' is disabled.")

    assigned_task = dict(task_definition)
    input_data = assigned_task.get("input_data", {})

    if not isinstance(input_data, dict):
        raise TypeError("input_data must be a dictionary")

    assigned_task["input_data"] = dict(input_data)
    assigned_task["input_data"]["employee_id"] = employee_id

    return assigned_task
