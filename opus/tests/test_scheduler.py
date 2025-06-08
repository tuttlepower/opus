from opus.models import Employee, Shift
from opus.scheduler import assign_shifts


def test_assign_shifts_basic():
    employees = [
        Employee(name="Alice", preferred_shift_length=8, availability=["morning"]),
        Employee(name="Bob", preferred_shift_length=8, availability=["morning"]),
    ]
    shifts = [Shift(start="morning", duration=8)]
    result = assign_shifts(employees, shifts)
    assert result[0].assigned_to in {"Alice", "Bob"}
