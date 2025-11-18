from django.contrib import admin
from .models import TestingDatabase, Student, Teacher, Courses, Subjects, Schedule

# Register your models here.
admin.site.register(TestingDatabase)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Schedule)
