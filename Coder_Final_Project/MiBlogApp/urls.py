from django.urls import URLPattern, path
from MiBlogApp import views
from .views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
]