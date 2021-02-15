from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentF
from .models import Student


# Create your views here.


def home(request):
    students = Student.objects.all()
    if request.method == 'POST':
        ff = StudentF(request.POST)
        if ff.is_valid():
            ff.save()
            return HttpResponseRedirect('/')

    else:
        ff = StudentF()
    return render(request, 'home.html', {'ff': ff, 'students': students})


def delete(request, id):
    if request.method == 'POST':
        std = Student.objects.get(pk=id)
        std.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def update(request, id):
    if request.method == 'POST':
        s = Student.objects.get(pk=id)
        ff = StudentF(request.POST,instance=s)
        if ff.is_valid():
            ff.save()
            return HttpResponseRedirect('/')
    else:
        s = Student.objects.get(pk=id)
        ff = StudentF(instance=s)
        return render(request, 'update.html', {'ff': ff})
