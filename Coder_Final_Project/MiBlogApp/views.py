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

    avatar=Avatar.objects.filter(user=request.user)
    return render(request, 'MiBlogApp/main.html' ,{'url': avatar[0].avatar.url})



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
            user=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
            user=authenticate(username=user, password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'MiBlogApp/index.html', {'user':user, 'message':'Welcome!'})
            else:
                return render(request, 'MiBlogApp/login.html', {'formulario':formulario, 'message':'Invalid username or password, try again'})
        else:
            return render(request, 'MiBlogApp/login.html', {'formulario':formulario, 'message':'Invalid username or password, try again'})
    
    else:
        formulario=AuthenticationForm()
        return render(request, 'MiBlogApp/login.html', {'formulario':formulario})


# Edit User Profile Views ---------------------------------------------------------------
@login_required
def editProfile(request):
    user=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=user)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            user.first_name=informacion['first_name']
            user.last_name=informacion['last_name']
            user.username=informacion['username']
            user.set_password(informacion['password1'])
            user.set_password(informacion['password2'])
            user.save()

            return render(request, 'MiBlogApp/index.html', {'user':user, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=user)
    return render(request, 'MiBlogApp/edit_profile.html', {'formulario':formulario, 'user':user.username})