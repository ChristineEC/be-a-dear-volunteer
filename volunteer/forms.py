from django import forms
from .models import Slot, Beneficiary


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['task',
            'task_location',
        ]

class SlotUpdateForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['task',
            'task_location',
            'date',
            'start_time',
            'end_time',
            'completed',
            'credit_minutes_requested',
            'credit_minutes_approved',
        ]
