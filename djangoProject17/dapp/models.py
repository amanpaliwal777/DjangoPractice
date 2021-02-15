from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.

class Statement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inde = models.CharField(max_length=10, blank=True)
    totalbal = models.IntegerField(default=0)
    bal = models.IntegerField()
