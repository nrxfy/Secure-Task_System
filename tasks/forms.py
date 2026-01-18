from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from .models import Profile 

class ProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile 
        fields = ['bio', 'avatar']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email'] # password fields are added automatically by UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']