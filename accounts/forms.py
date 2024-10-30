from django import forms
from django.forms import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=PasswordInput)
    password_confirmation = forms.CharField(
        max_length=150, widget=PasswordInput
    )
