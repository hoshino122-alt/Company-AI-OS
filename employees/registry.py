"""Employee registry for Company AI OS."""

from employees.definitions import EMPLOYEES


def list_employees(enabled_only=False):
    """Return registered employees without exposing internal instructions."""
    employees = []

    for employee_id, employee in EMPLOYEES.items():
        if enabled_only and not employee.get("enabled", False):
            continue

        employees.append({
            "employee_id": employee_id,
            "name": employee["name"],
            "responsibility": employee["responsibility"],
            "enabled": employee.get("enabled", False),
        })

    return employees


def get_employee(employee_id):
    """Return public information for one employee, or None if not found."""
    employee = EMPLOYEES.get(employee_id)

    if employee is None:
        return None

    return {
        "employee_id": employee_id,
        "name": employee["name"],
        "responsibility": employee["responsibility"],
        "enabled": employee.get("enabled", False),
    }
