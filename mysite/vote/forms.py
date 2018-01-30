from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'name': 'username', 'placeholder': 'username', 'required': 'required'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'name': 'password', 'placeholder': 'password', 'required': 'required'

    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'name': 'password', 
        'placeholder': 'confirm-password', 'required': 'required'}))


class VotingForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'name': 'name', 
         'placeholder': 'Enter the candidate name,, e.g Smith Neil', 
         'required': 'required'


    }))
