from django import forms

class dform(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)