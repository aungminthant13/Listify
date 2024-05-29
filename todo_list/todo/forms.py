from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tasks


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)

    class Meta:
        model = Tasks
        fields = ['title', 'description', 'date', 'time', 'complete']
