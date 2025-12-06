from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    all_product = Product.objects.all()
    return render(request, 'index.html', {"products": all_product})