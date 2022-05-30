from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Re-enter password", widget=forms.PasswordInput)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name= forms.CharField(label="Update Name")
    last_name= forms.CharField(label="Update Surname")
    username= forms.CharField(label="Update Username", required=True)
    password1= forms.CharField(label="Update Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Re-enter updated password", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'password1', 'password2')
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar= forms.ImageField(label="Avatar")