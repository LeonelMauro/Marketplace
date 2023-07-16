from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nombre del usuario',
        'class': 'w-full py-4 px-6 rounded-lx'
    }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Tu contrañesa',
        'class': 'w-full py-4 px-6 rounded-lx'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nombre del usuario',
        'class': 'w-full py-4 px-6 rounded-lx'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Tu Email',
        'class': 'w-full py-4 px-6 rounded-lx'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Tu contrañesa',
        'class': 'w-full py-4 px-6 rounded-lx'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repita contraseña',
        'class': 'w-full py-4 px-6 rounded-lx'
    }))