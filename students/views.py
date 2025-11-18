from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    return HttpResponse('Hi students')

def greet(request):
    return HttpResponse('kamusta ka bai')