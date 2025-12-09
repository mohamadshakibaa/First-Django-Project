from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.contrib import messages

def home(request):
    all_product = Product.objects.all()
    return render(request, 'index.html', {"products": all_product})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "exit seccessful")
    return redirect('home')