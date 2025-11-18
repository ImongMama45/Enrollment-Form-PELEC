from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student, Teacher,Courses, Subjects, Schedule
from .forms import Student_Form

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

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = Student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Student')  
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
        form = Student_Form(instance=student)
    return render(request,'online_enrollment//Student_Edit.html', {'form': form, 'student': student})

def add_teacher(request):
    if request.method == 'POST':
        form = Student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Test_Student')  # Redirect to a list of students after saving
    else:
        form = Student_Form()
    return render(request, 'online_enrollment//Teacher_Forms.html', {'form': form})

def edit_teacher(request, pk):
    student = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        form = Student_Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('Test_Teacher')
        form = Student_Form(instance=student)
    return render(request,'online_enrollment//Teacher_Edit.html', {'form': form, 'student': student})

