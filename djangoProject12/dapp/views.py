from django.shortcuts import render, HttpResponseRedirect
from .forms import signup
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# this is for signup
def home(request):
    if request.method == 'POST':
        ff = signup(request.POST)
        if ff.is_valid():
            ff.save()
            messages.success(request, 'your registration is done')
            ff = signup()
    else:
        ff = signup()
    return render(request, 'home.html', {'ff': ff})


# login views function

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            ff = AuthenticationForm(request=request, data=request.POST)
            if ff.is_valid():
                uname = ff.cleaned_data['username']
                upass = ff.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    messages.success(request, 'login succcessfull')
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            ff = AuthenticationForm()
        return render(request, 'login.html', {'ff': ff})
    else:
        return HttpResponseRedirect('/profile/')


# this is profile
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')



#this is log out

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')