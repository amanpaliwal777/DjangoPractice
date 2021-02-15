from django import forms
from django.core import validators

def clean_name(value):
    if len(value) < 5:
        raise forms.ValidationError('name should be more than 5 char')
def email(value):
    if len(value) < 10:
        raise forms.ValidationError('email should be more than 10')


class dform(forms.Form):
    name = forms.CharField(validators=[clean_name])
    email = forms.EmailField(validators=[email])
