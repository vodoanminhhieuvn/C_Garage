from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileAdditional


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2','is_staff']

# Where we create 2 different forms and save it at the site

class UserUpdateForm(forms.ModelForm):    
    class Meta:
        model = User
        fields = ['password1', 'password2', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileAdditional
        fields = ['image']
