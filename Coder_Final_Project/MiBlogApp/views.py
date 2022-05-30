from django.shortcuts import render
from django import http
from .models import *
# Create your views here.

def inicio(request):
    return render(request, 'MiBlogApp/father.html')