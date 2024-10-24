from django.shortcuts import render
from .models import Product

def home(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'products':products})

def about(request):
	return render(request, 'about.html',{})