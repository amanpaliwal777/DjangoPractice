from django.db import models


# Create your models here.
class Enroll(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
