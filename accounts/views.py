from django.shortcuts import render, redirect
from django.views import View
from .models import User
# Create your views here.

class LoginView(View):
    def get(self, request):
        model=User
        context={
            "model":model
        }
        return render(request, "accounts/login.html", context)
    
    