from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learndj(request):
    # return HttpResponse('learndj')
    return render(request,'proapp1/cdj.html',{'django':'this is django course'})

def learnpy(request):
    # return HttpResponse('learnpy')
    return render(request,'proapp1/cpy.html',{'python':'this is Python course'})