from django.db import models

# Create your models here.
class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Student(models.Model):
    student_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course_enrolled = models.CharField(max_length=100)
    year_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Teacher(models.Model):
    subjects_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Courses(models.Model):
    student_enrolled = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    teachers = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Subjects(models.Model):
    subjects_id = models.CharField()
    grades = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    student_enrolled = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Schedule(models.Model):
    subjects = models.CharField(max_length=100)
    teachers = models.CharField(max_length=100)
    days = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.days}"

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"