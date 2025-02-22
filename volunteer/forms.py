from django import forms
from .models import Slot


class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = [
                    'task',
                    'task_location',
                    'dates',
                    'times',
                    'completed',
                    'credit_minutes_requested',
                ]
