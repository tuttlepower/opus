from __future__ import annotations

from collections import defaultdict
from typing import List

from .models import Employee, Shift


def assign_shifts(employees: List[Employee], shifts: List[Shift]) -> List[Shift]:
    """Assign shifts to employees with a simple fairness heuristic."""
    # Track undesirable shift counts
    undesired_counts = defaultdict(int)
    for emp in employees:
        undesired_counts[emp.name] = emp.undesirable_shifts

    for shift in shifts:
        # Find all available employees for the shift
        available = [e for e in employees if shift.start in e.availability]
        # Sort by number of undesirable shifts and seniority
        available.sort(key=lambda e: (undesired_counts[e.name], -e.seniority))
        if available:
            chosen = available[0]
            shift.assigned_to = chosen.name
            # Update counts if shift duration differs from preference
            if shift.duration != chosen.preferred_shift_length:
                undesired_counts[chosen.name] += 1
        else:
            shift.assigned_to = None
    return shifts
