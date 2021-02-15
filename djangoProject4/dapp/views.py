from django.shortcuts import render
from .forms import dform


# Create your views here.
def home(request):
    if request.method == 'POST':
        ff = dform(request.POST)
        if ff.is_valid():
            name = ff.cleaned_data['name']
            email = ff.cleaned_data['email']
            password = ff.cleaned_data['password']
            print(name,email,password)

        return render(request, 'home.html', {'ff': ff})
    else:
        ff = dform()
        return render(request, 'home.html', {'ff': ff})
