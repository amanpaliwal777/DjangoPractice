from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import UserCreate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from .models import Statement


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = UserCreate(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'your registration is successfull <br> account created with zero balance')
                data = User.objects.get(username=forms.cleaned_data['username'])
                data1 = Statement(user_id=data.id, bal=0)
                data1.save()

        else:
            forms = UserCreate()
        return render(request, 'home.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/profile/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = AuthenticationForm(request=request, data=request.POST)
            if forms.is_valid():
                uname = forms.cleaned_data['username']
                upass = forms.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login successfull!!!')
                    return HttpResponseRedirect('/profile/')
            return HttpResponse('form is invalid')

        else:
            forms = AuthenticationForm()
        return render(request, 'login.html', {'forms': forms})
    else:
        return render(request, 'profile.html', {'name': request.user})


def user_profile(request):
    if request.user.is_authenticated:
        statements = Statement.objects.filter(user=request.user.id)
        if request.method == 'POST':
            balance = request.POST.get('balance')
            inde = request.POST.get('inde')
            totalbal = Statement.objects.filter(user_id=request.user.id).last().totalbal
            if inde == 'i':
                totalbal = int(totalbal) + int(balance)
            else:
                totalbal = int(totalbal) - int(balance)
            data = Statement(user_id=request.user.id, inde=inde, totalbal=totalbal, bal=balance)
            data.save()
            messages.success(request, 'Balance updated')
            return HttpResponseRedirect('/profile/')
        else:
            statements = Statement.objects.filter(user=request.user.id)
        return render(request, 'profile.html', {'name': request.user, 'statements': statements})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def defaultPrinting(request):
    totalbal = Statement.objects.filter(user_id=request.user.id).last()
    print(totalbal.totalbal)
    return HttpResponseRedirect('/login/')
