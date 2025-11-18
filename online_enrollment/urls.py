from django.urls import path
from . import views

urlpatterns = [
    path('Test_Student/', views.Test_Student, name='Test_Student'),
    path('Test_Teacher/', views.Test_Teacher, name='Test_Teacher'),
    path('Test_Course/', views.Test_Course, name='Test_Course'),
    path('Test_Subjects/', views.Test_Subjects, name='Test_Subjects'),
    path('Test_Schedule/', views.Test_Schedule, name='Test_Schedule'),
    path('Student_Form/', views.add_student, name='Test_Schedule'),
    path('Teacher_Form/', views.add_teacher, name='Test_Schedule'),
    path('Student_Edit/<int:pk>/', views.edit_student, name='Test_Schedule'),
    path('Teacher_Edit/<int:pk>/', views.edit_teacher, name='Test_Schedule'),
]

