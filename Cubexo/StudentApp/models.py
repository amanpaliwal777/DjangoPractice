from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    classes = models.IntegerField()
    division = models.CharField(max_length=10)
    age = models.IntegerField()
