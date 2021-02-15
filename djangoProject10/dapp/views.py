from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import signupf
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='POST':
        ff = signupf(request.POST)
        if ff.is_valid():
            ff.save()
            messages.success(request,'your registration is done')
            ff= signupf()
    else:
        ff = signupf()
    return render(request,'home.html',{'ff':ff})