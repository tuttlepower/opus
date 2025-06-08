from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    preferred_shift_length = models.IntegerField(default=8)
    seniority = models.IntegerField(default=0)
    undesirable_shifts = models.IntegerField(default=0)
    availability = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Shift(models.Model):
    start = models.CharField(max_length=100)
    duration = models.IntegerField()
    assigned_to = models.ForeignKey(
        Employee,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_shifts',
    )

    def __str__(self):
        return f"{self.start} ({self.duration}h)"
