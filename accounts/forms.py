from django.contrib.auth.models import AuthenticationForm
from django import forms

class CustomAuthForm(AuthenticationForm):
    username=forms.CharField()
    password=forms.CharField()
    