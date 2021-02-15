from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
