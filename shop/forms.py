from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
    
    
class SingUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your firstname'})
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your lastname'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email address'})
    )
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Enter your password'
            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Enter your password again'
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2')