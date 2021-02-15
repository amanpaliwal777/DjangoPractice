from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from django.db.models import Q


# Create your views here.

def home(request):
    students = Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        classes = request.POST.get('classes')
        division = request.POST.get('division')
        age = request.POST.get('age')
        data = Student(
            name=name,
            phone=phone,
            email=email,
            classes=classes,
            division=division,
            age=age
        )
        data.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'home.html', {'students': students})


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
        s.name = request.POST.get('name')
        s.phone = request.POST.get('phone')
        s.email = request.POST.get('email')
        s.classes = request.POST.get('classes')
        s.division = request.POST.get('division')
        s.age = request.POST.get('age')
        s.save()
        return HttpResponseRedirect('/')
    else:
        s = Student.objects.get(pk=id)
        return render(request, 'update.html', {'s': s})


def search(request):
    if request.method == 'POST':
        classes = request.POST.get('classes')
        division = request.POST.get('division')
        students = Student.objects.filter(Q(classes__exact=classes)|Q(division__contains=division))
    else:
        students = Student.objects.all()
    return render(request, 'search.html', {'students': students})
