from django import forms


class dform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 3:
            raise forms.ValidationError('please enter more than 3 char')
        return valname
