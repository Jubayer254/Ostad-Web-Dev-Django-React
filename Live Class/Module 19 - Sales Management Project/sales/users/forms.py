from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
    }))

class OTPForm(forms.Form):
    otp = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter OTP',
    }))