from django.shortcuts import render
from .forms import dform


# Create your views here.
def home(request):
    if request.method == "POST":
        ff = dform(request.POST)
        if ff.is_valid():
            name = ff.cleaned_data['name']
            email = ff.cleaned_data['email']
            print(name, email)
            ff =dform()
        
    else:
        ff = dform()
    return render(request, 'home.html', {'ff': ff})
