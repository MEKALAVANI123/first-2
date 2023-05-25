from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def student(request):
    return HttpResponse('<h2>Education is very important</h2>')

def registration(request):
    return HttpResponse('<h1>To join in School registration must and should')