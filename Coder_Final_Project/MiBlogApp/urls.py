from django.urls import URLPattern, path
from MiBlogApp import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('register', views.register, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', LogoutView.as_view(template_name="MiBlogApp/logout.html"), name='logout'),

    path('editProfile', views.editProfile, name='editProfile'),

    path('pages/list/', ViewPages.as_view(), name='view_pages'),
    path('pages/list/<pk>', DetailPage.as_view(), name='detail_page'),
    path('pages/new/',CreatePage.as_view(), name='create_page'),
    path('pages/edit/<pk>', EditPage.as_view(), name='edit_page'),
    path('pages/delete/<pk>', DeletePage.as_view(), name='delete_page'),


]