from django.shortcuts import render
from .models import Enroll
from .forms import EnrollForm


def home(request):
    ab = {'roll': '123', 'name': 'aman', 'email': 'amanpaliwal777@gmail.com', 'mobile': '8982516018'}
    ffm = EnrollForm(initial=ab)
    return render(request, 'home.html', {'ffm': ffm})


def fee(request):
    return render(request,'fees.html')

def course(request):
    return render(request,'course.html')