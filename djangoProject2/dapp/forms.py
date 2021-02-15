from django import forms


class dappform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 3:
            raise forms.ValidationError('name should be more than 3 char')
        return valname