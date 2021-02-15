from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'projectapp/home.html', {'home': 'its home.html files'})


def python(request):
    return render(request, 'projectapp/python.html', {'cor': 'python'})


def django(request):
    return render(request, 'projectapp/django.html', {'cor': 'django'})
