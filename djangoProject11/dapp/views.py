from django.shortcuts import render
from .forms import signupform
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        ff = signupform(request.POST)
        if ff.is_valid():
            ff.save()
            messages.success(request,'your reigstration is done')
            ff = signupform()
    else:
        ff = signupform()
    return render(request,'signupform.html',{'ff':ff})