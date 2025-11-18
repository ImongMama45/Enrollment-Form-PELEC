from django import forms
from .models import Student, Courses, Teacher, Subjects, Schedule

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name','course_enrolled',]
        
class Student_Form_Edit(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name','course_enrolled',]

class Teacher_Form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subjects_id','name','department','email','address']


class Teacher_Form_Edit(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subjects_id','name','department','email','address']
