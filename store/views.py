from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def home(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'products':products})

def register_user(request):
    form = SignUpForm()
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate & Login the User
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You have registered successfully.")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed. Please log in manually.")
                return redirect('login')
        else:
            messages.error(request, "Error occurred! Please check the form.")
    
    return render(request, 'register.html', {'form': form})

def about(request):
	return render(request, 'about.html',{})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")  # Success message
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")  # Error message
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request,("You have been logged out."))
	return redirect('home')