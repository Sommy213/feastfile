from django import forms
from .models import WeEat
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = WeEat
        fields = ['title', 'price', 'image','body']
        
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


