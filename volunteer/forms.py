from django import forms
from .models import Slot


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['task',
                'task_location',
                'date',
                'start_time',
                'end_time',
                'completed',
                'credit_minutes_requested',
                ]


