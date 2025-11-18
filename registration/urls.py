from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('congrats/', views.congrats, name='congrats'),
]

