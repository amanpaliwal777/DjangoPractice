from django.contrib import admin
from .models import Statement


# Register your models here.

@admin.register(Statement)
class AdminStatemen(admin.ModelAdmin):
    list_display = ['user','totalbal', 'bal', 'inde']
