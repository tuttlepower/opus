from dataclasses import dataclass, field
from typing import List

@dataclass
class Employee:
    name: str
    preferred_shift_length: int  # hours
    seniority: int = 0
    undesirable_shifts: int = 0
    availability: List[str] = field(default_factory=list)

@dataclass
class Shift:
    start: str  # e.g. '2023-01-01 09:00'
    duration: int  # hours
    assigned_to: str | None = None
