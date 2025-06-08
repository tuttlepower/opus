import csv
from pathlib import Path
from typing import List

from .models import Employee, Shift
from .scheduler import assign_shifts


def load_employees(csv_path: Path) -> List[Employee]:
    employees = []
    with csv_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            availability = row.get("availability", "").split("|") if row.get("availability") else []
            employees.append(
                Employee(
                    name=row["name"],
                    preferred_shift_length=int(row.get("preferred_shift_length", 8)),
                    seniority=int(row.get("seniority", 0)),
                    undesirable_shifts=int(row.get("undesirable_shifts", 0)),
                    availability=availability,
                )
            )
    return employees


def load_shifts(csv_path: Path) -> List[Shift]:
    shifts = []
    with csv_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            shifts.append(Shift(start=row["start"], duration=int(row["duration"])))
    return shifts


def run(employees_csv: str, shifts_csv: str) -> List[Shift]:
    employees = load_employees(Path(employees_csv))
    shifts = load_shifts(Path(shifts_csv))
    assigned = assign_shifts(employees, shifts)
    return assigned


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run Opus scheduler")
    parser.add_argument("employees", help="CSV file with employee data")
    parser.add_argument("shifts", help="CSV file with shift requirements")
    args = parser.parse_args()
    result = run(args.employees, args.shifts)
    for shift in result:
        print(f"{shift.start}: {shift.duration}h -> {shift.assigned_to}")
