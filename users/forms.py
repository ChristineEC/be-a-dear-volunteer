from django import forms
from .models import Profile
from volunteer.models import Homeroom

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'alias',
            'homeroom',
            'profile_pic'
        ]
