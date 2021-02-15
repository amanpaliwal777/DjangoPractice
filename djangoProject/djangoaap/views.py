from django.shortcuts import render
from .models import Student
from .forms import StudentForm


# Create your views here.

def home(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, 'homepage.html', context=context)


def inserts(request):
    if request.method == 'POST':
        values = StudentForm(request.POST)
        if values.is_valid():
            student_name = request.POST.get('student_name')
            student_class = request.POST.get('student_class')
            student_subject = values.cleaned_data.get('student_subject')
            student_marks = values.cleaned_data.get('student_marks')
            data = Student(
                student_name=student_name,
                student_class = student_class,
                student_marks = student_marks,
                student_subject = student_subject
            )
            data.save()
            studentform = StudentForm
            return render(request, 'insert.html', {'studentform': studentform})

    else:
        studentform = StudentForm
        return render(request, 'insert.html', {'studentform': studentform})
