from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import registration
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def registrations(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = registration(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your registration is done !!!')
                form = registration()
        else:
            form = registration()
        return render(request, 'registration.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


# this is for login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login successfull !!!')
                    return HttpResponseRedirect('/profile/')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# changing the password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'password change successfully !!!')
                return HttpResponseRedirect('/profile/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': form})
    else:
        messages.error(request, 'you have to login first')
        return HttpResponseRedirect('/login/')


def user_setpass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'setpass.html', {'form': form})
    else:
        messages.error(request, 'login first')
        return HttpResponseRedirect('/login/')
