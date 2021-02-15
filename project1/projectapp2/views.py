from django.shortcuts import render


def feedj(request):
    return render(request,'proapp2/fdj.html',{'django':'this is django course fee 300'})

def feepy(request):
    return render(request,'proapp2/fpy.html',{'python':'this is Python course fee 200'})
