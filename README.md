# Opus Scheduler

Opus is a simple scheduling tool intended to help managers distribute shifts
fairly among employees. This project provides a basic Python implementation that
can be extended for more complex use cases.

## Features

- Employees can specify preferred shift lengths and availability.
- Fair assignment of shifts based on seniority and history of undesirable shifts.
- CSV import for employee and shift data.
- Command line interface for generating a schedule.

## Usage

Create two CSV files: one for employees and one for shifts.

`employees.csv`:
```
name,preferred_shift_length,seniority,undesirable_shifts,availability
Alice,8,1,0,morning|evening
Bob,8,2,0,morning
```

`shifts.csv`:
```
start,duration
morning,8
evening,8
```

Run the scheduler:
```
python -m opus.main employees.csv shifts.csv
```

The tool will print the assigned employee for each shift.

## Monetization

This repository does not implement licensing or subscription checks.
You can extend the CLI to require a license key or integrate with a payment
processor when you turn Opus into a commercial product.

## Django Front End

A minimal Django project is included for managing employees and shifts via the
Django admin site. Install Django and run migrations:

```bash
pip install django
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

Then visit `http://localhost:8000/` to see the schedule or `/admin/` to edit
records.
