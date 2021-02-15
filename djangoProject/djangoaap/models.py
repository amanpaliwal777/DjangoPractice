from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    SUBJECT_choice = (
        ('CS', 'Computer Science'),
        ('CE', 'Civil'),
        ('ME', 'Mechanical')
    )
    student_subject = MultiSelectField(max_length=20, choices=SUBJECT_choice)
    student_marks = models.IntegerField()
