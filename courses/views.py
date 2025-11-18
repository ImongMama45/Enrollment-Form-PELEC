from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('HELLO WORLD!')


def coursesDisplay(request):
    return HttpResponse('BSIT - 3B')