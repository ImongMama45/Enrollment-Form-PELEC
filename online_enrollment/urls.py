from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Test_Student/', views.Test_Student, name='Test_Student'),
    path('Test_Teacher/', views.Test_Teacher, name='Test_Teacher'),
    
    path('Test_Course/', views.Test_Course, name='Test_Course'),
    path('Test_Subjects/', views.Test_Subjects, name='Test_Subjects'),

    path('Test_Schedule/', views.Test_Schedule, name='Test_Schedule'),

    path('Student_Form/', views.add_student, name='Student_Form'),
    path('Teacher_Form/', views.add_teacher, name='Teacher_Form'),

    path('Student_Edit/<int:pk>/', views.edit_student, name='Student_Edit'),
    path('Teacher_Edit/<int:pk>/', views.edit_teacher, name='Teacher_Edit'),

    path('Course_Form/', views.add_course, name='Course_Form'),
    path('Course_Edit/<int:pk>/', views.edit_course, name='Course_Edit'),
    path('Subjects_Form/', views.add_subjects, name='Subjects_Form'),
    path('Subjects_Edit/<int:pk>/', views.edit_subjects, name='Subjects_Edit'),
    path('Schedule_Form/', views.add_schedule, name='Schedule_Form'),
    path('Schedule_Edit/<int:pk>/', views.edit_schedule, name='Schedule_Edit'),

    path('Logins/', views.login_user, name='Logins'),
    path('Logout/', views.logout_user, name='Logout'),
    path('Registers/', views.register_user, name='Registers'),
]