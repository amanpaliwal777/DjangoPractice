from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class signupform(UserCreationForm):
    password2 = forms.CharField(
        label='Password (again)',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
