from django.shortcuts import render
from django import http
from .models import *
from .forms import *
# Create your views here.

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def main(request):
    return render(request, 'MiBlogApp/main.html')



# Register and Login/Logout Views ---------------------------------------------------------------

def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'MiBlogApp/index.html', {'message':f'{username}. The user was successfully created!'})
        else:
            return render(request, 'MiBlogApp/index.html', {'message':'User could not be created'})
    else:
        formulario = UserRegistrationForm()
        return render(request, 'MiBlogApp/register.html', {'formulario':formulario})

def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
            user=authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'MiBlogApp/index.html', {'user':usuario, 'message':'Welcome!'})
            else:
                return render(request, 'MiBlogApp/login.html', {'formulario':formulario, 'message':'Invalid username or password, try again'})
        else:
            return render(request, 'MiBlogApp/login.html', {'formulario':formulario, 'message':'Invalid username or password, try again'})
    
    else:
        formulario=AuthenticationForm()
        return render(request, 'MiBlogApp/login.html', {'formulario':formulario})
