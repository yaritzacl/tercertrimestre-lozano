#from django.contrib import admin
#from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

#def home(request):
#    return HttpResponse('<h1> Hola mundo ')

def home(request):
    return render(request,'home.html')