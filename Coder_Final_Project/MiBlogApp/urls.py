from django.urls import URLPattern, path
from MiBlogApp import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.main, name='main'),

    path('register', views.register, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', LogoutView.as_view(template_name="MiBlogApp/logout.html"), name='logout'),

    path('editProfile', views.editProfile, name='editProfile'),
]