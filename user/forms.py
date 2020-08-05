from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'placeholder' : 'email'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'user name'
        }
    ))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")


