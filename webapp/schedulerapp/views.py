from django.shortcuts import render
from .models import Shift


def schedule_view(request):
    shifts = Shift.objects.select_related('assigned_to').all()
    return render(request, 'schedulerapp/schedule.html', {'shifts': shifts})
