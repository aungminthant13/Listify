from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks  # Import from current directory (tasks)


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields["username"].widget.attrs.update({
          'required':'',
          'name': 'username',
          'id': 'username',
          'type': 'text',
          'class': 'login_form',
          'placeholder': 'Username',
          'maxlength': '20',
          'minlength': '6'
      })

      self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'first_name', 
            'id':'first_name', 
            'class': 'login_form',
            'type':'text', 
            'placeholder':'First Name'
      })

      self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'last_name', 
            'id':'last_name',
            'class': 'login_form', 
            'type':'text', 
            'placeholder':'Last Name',
      })

      self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email',
            'class': 'login_form', 
            'type':'email', 
            'placeholder':'Email'
      })
      
      self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'class': 'login_form',
            'type': 'password',
            'placeholder': 'Password',
            'maxlength': 22,
            'minlength': 8
      })

      self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2',
            'class': 'login_form', 
            'type':'password', 
            'placeholder':'Confirm password', 
            'maxlength':'22',  
            'minlength':'8' 
      }) 

      username = forms.CharField(max_length=20, label=False) 
      email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']