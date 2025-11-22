from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Courses, Teacher, Subjects, Schedule

# Student Forms

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name','course_enrolled',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })
class Student_Form_Edit(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name','course_enrolled',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })
# Teacher Forms

class Teacher_Form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subjects_id','name','department','email','address']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })

class Teacher_Form_Edit(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subjects_id','name','department','email','address']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })
# Courses Forms

class Course_Form(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['student_enrolled', 'name', 'department', 'teachers', 'subjects']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })

class Course_Form_Edit(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['student_enrolled','name','department','teachers','subjects']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })
# Schedule Forms

class Schedule_Form(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['subjects','teachers','days','time_slot','course']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })

class Schedule_Form_Edit(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['subjects','teachers','days','time_slot','course']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })
# Subjects Forms
class Subjects_Form(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subjects_id','grades','name','student_enrolled','course']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })
class Subjects_Form_Edit(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subjects_id','grades','name','student_enrolled','course']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })

# User Registration Form
class UserRegister_Form(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%; padding:12px 15px; border:2px solid #e0e0e0; border-radius:8px; font-size:14px; box-sizing:border-box;'
            })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text from all fields
        for field in self.fields.values():
            field.help_text = ''
