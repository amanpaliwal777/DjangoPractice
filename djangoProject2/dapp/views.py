from django.shortcuts import render
from .forms import dappform
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
    if request.method == "POST":
        ff = dappform(request.POST)
        if ff.is_valid():
            name = ff.cleaned_data['name']
            email = ff.cleaned_data['email']
            password = ff.cleaned_data['password']
            print(name, email, password)
        return HttpResponseRedirect('/thanks')

    else:
        ff = dappform()
        return render(request, 'home.html', {'ff': ff})


def thanks(request):
    return render(request, 'thanks.html')
