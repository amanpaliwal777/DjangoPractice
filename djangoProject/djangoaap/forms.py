from django import forms
from multiselectfield import MultiSelectFormField


class StudentForm(forms.Form):
    student_name = forms.CharField(
        label='Your name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'enter your name',
                'class': 'form-control'
            }
        )
    )

    student_class = forms.IntegerField(
        label='class',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'class',
                'class': 'form-control'
            }
        )
    )

    SUBJECT_choice = (
        ('CS', 'Computer Science'),
        ('CE', 'Civil'),
        ('ME', 'Mechanical')
    )
    student_subject = MultiSelectFormField(
        max_length=20,
        choices=SUBJECT_choice,
        label='subject',
    )
    student_marks = forms.IntegerField(
        label='your marks',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'marks',
                'class': 'form-control'
            }
        )
    )
