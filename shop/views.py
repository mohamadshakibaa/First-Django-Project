from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.contrib import messages
from .forms import SingUpForm

def home(request):
    all_product = Product.objects.all()
    return render(request, 'index.html', {"products": all_product})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "successfuly Enter")
            return redirect('home')
        else:
            messages.success(request, 'we have a problem')
            return redirect('login')
        
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "exit seccessful")
    return redirect('home')


def signup_user(request):
    form = SingUpForm()
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ('Account created'))
            return redirect('home')
        else:
            messages.error(request, ('Could not authenticate after signup. Try logging in.'))
            return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'signup.html', {'form': form})