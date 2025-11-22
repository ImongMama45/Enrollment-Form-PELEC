from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Student, Teacher,Courses, Subjects, Schedule
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Teacher, Courses, Subjects, Schedule
from django.contrib.auth.decorators import login_required
from .forms import UserRegister_Form,Student_Form, Student_Form_Edit, Teacher_Form, Teacher_Form_Edit, Course_Form, Course_Form_Edit, Schedule_Form, Schedule_Form_Edit, Subjects_Form, Subjects_Form_Edit 

# Create your views here.
def Test_Student(request):
    student = Student.objects.all()
    return render(request, 'online_enrollment//base.html', {'Student':student})

def Test_Teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'online_enrollment//Teacher.html', {'Teacher':teacher})

def Test_Course(request):
    courses = Courses.objects.all()
    return render(request, 'online_enrollment//Courses.html', {'Courses':courses})

def Test_Subjects(request):
    subjects = Subjects.objects.all()
    return render(request, 'online_enrollment//Subjects.html', {'Subjects':subjects})

def Test_Schedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'online_enrollment//Schedule.html', {'Schedule':schedule})

def Home(request):
    student = Student.objects.all()
    return render(request, 'online_enrollment//Home.html', {'student': student})

# Student Forms

def add_student(request):
    if request.method == 'POST':
        form = Student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Student')  
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Student_Form()
    return render(request, 'online_enrollment//Student_Form.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = Student_Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('Test_Student')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Student_Form(instance=student)
    return render(request,'online_enrollment//Student_Edit.html', {'form': form, 'student': student})

# Teacher Forms

def add_teacher(request):
    if request.method == 'POST':
        form = Teacher_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Teacher')  # Redirect to a list of teachers after saving
        else:
            messages.error(request, "There was an error with your submission.")   
    else:
        form = Teacher_Form()
    return render(request, 'online_enrollment//Teacher_Forms.html', {'form': form})

def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = Teacher_Form_Edit(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('Test_Teacher')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Teacher_Form_Edit(instance=teacher)
    return render(request,'online_enrollment//Teacher_Edit.html', {'form': form, 'teacher': teacher})

# Courses Forms

def add_course(request):
    if request.method == 'POST':
        form = Course_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Course')  
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Course_Form()
    return render(request, 'online_enrollment//Course_Form.html', {'form': form})   
def edit_course(request, pk):   
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        form = Course_Form(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('Test_Course')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Course_Form(instance=course)
    return render(request,'online_enrollment//Course_Edit.html', {'form': form, 'course': course})


# Schedule Forms
def add_schedule(request):
    if request.method == 'POST':
        form = Schedule_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Schedule')
        else:
            messages.error(request, "There was an error with your submission.")  
    else:
        form = Schedule_Form()
    return render(request, 'online_enrollment//Schedule_Form.html', {'form': form})

def edit_schedule(request, pk):
    if request.method == 'POST':
        form = Schedule_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Schedule')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Schedule_Form() 
    return render(request, 'online_enrollment//Schedule_Edit.html', {'form': form})

# Subjects Forms    

def add_subjects(request):
    if request.method == 'POST':
        form = Subjects_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Subjects')  
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Subjects_Form()
    return render(request, 'online_enrollment//Subject_Form.html', {'form': form})

def edit_subjects(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        form = Subjects_Form(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('Test_Subjects')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = Subjects_Form(instance=subject)
    return render(request,'online_enrollment//Subject_Edit.html', {'form': form, 'subject': subject})

#Login and Register Views
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'online_enrollment//Login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegister_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f"Account created for {username}!")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('Logins')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserRegister_Form()
    return render(request, 'online_enrollment/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('Logins')