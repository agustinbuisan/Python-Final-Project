from cmath import log
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

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


def main(request):
    return render(request, 'MiBlogApp/father.html')

def home(request):
    avatar=Avatar.objects.filter(user=request.user)
    return render(request, 'MiBlogApp/index.html',{'message':f'Welcome {request.user}!', 'avatar':avatar})
    
def about(request):
    return render(request, 'MiBlogApp/about.html')

# Register and Login/Logout Views ---------------------------------------------------------------

def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'MiBlogApp/index.html', {'message':f'User {username} was successfully created! Log in now!'})
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
                return render(request, 'MiBlogApp/index.html', {'message':f'Welcome {user}!'})
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

            return render(request, 'MiBlogApp/index.html', {'message':f'{user.username} was successfully updated!'})
    else:
        formulario=UserEditForm(instance=user)
    return render(request, 'MiBlogApp/edit_profile.html', {'formulario':formulario, 'user':user.username})


#Pages Views ---------------------------------------------------------------

#Create Page
class CreatePage(CreateView):
    model = Pages
    fields = ['user', 'author', 'title', 'subtitle', 'body', 'image']
    success_url = reverse_lazy('view_pages')

#View list of Pages
class ViewPages(ListView):
    model = Pages
    template_name = 'MiBlogApp/view_pages.html'

#View detail of Pages
class DetailPage(DetailView):
    model = Pages
    template_name = 'MiBlogApp/detail_page.html'

#Edit Page
class EditPage(UpdateView):
    model = Pages
    fields = ['author', 'title', 'subtitle', 'body', 'image']
    success_url = reverse_lazy('view_pages')

#Delete Page
class DeletePage(DeleteView):
    model = Pages
    fields = ['author', 'title', 'subtitle', 'body', 'image']
    success_url = reverse_lazy('view_pages')
    