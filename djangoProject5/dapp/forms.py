from django import forms

class dform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 3:
            raise forms.ValidationError('should be more than 3')
        return valname
