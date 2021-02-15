from django.contrib import admin
from  .models import  Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','classes','division','age']