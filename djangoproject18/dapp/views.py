from django.shortcuts import render, HttpResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse


# Create your views here.
def home(request):
    stu = Student.objects.get(pk=3)
    print(stu)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)
    # print(serializer)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')


def second(request):
    stu = Student.objects.all()
    print(stu)
    serializer = StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)
    # print(serializer)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
