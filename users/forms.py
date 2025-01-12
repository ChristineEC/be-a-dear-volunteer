from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterUser(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            )
