from django.shortcuts import render, HttpResponseRedirect
from .forms import signup_form,EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# Create your views here.

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signup_form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration successfull!!!')
                form = signup_form()
        else:
            form = signup_form()
        return render(request, 'sign_up.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


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
                    messages.success(request, 'login successful !!!')
                    return HttpResponseRedirect('/profile/')
        else:
            form = AuthenticationForm()
        return render(request, 'Log_in.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser:
                form = EditAdminProfileForm(instance=request.user,data=request.POST)
            else:
                form = EditUserProfileForm(instance=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'profile updated')
                return HttpResponseRedirect('/profile/')
        else:
            if request.user.is_superuser:
                form = EditAdminProfileForm(instance=request.user)
            else:
                form = EditUserProfileForm(instance=request.user)
        return render(request,'profile.html',{'name':request.user,'form':form})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'password changed successfully !!!')
                return HttpResponseRedirect('/profile/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')