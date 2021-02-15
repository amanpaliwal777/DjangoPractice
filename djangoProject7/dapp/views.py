from django.shortcuts import render
from .forms import dform
from .models import Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        ff = dform(request.POST)
        if ff.is_valid():
            ff.save()
            ff = dform()
    else:
        ff = dform()
    return render(request,'home.html',{'ff':ff})