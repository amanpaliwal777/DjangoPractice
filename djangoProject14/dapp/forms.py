from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','last_login','date_joined']
        labels = {'email':'Email'}