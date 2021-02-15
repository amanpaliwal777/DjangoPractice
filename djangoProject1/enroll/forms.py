from django import forms


class EnrollForm(forms.Form):
    roll = forms.IntegerField()
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()

