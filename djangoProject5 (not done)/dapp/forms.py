from django import forms


class dform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def clean_name(self):
        # cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        # valemail = self.cleaned_data['email']
        if len(valname) < 150:
            raise forms.ValidationError('name should be more than 3 char')
        # if len(valemail) < 14:
        #     print('email wala')
        #     raise forms.ValidationError('enter more than 14 characters')
        return valname
