from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def restrict_logged_in_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to a home page or dashboard
        return view_func(request, *args, **kwargs)
    return wrapper

def create_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        # Validate that first and last names are provided
        if not first_name or not last_name:
            messages.error(request, "First name and last name are required!")
            return render(request, 'website/signup.html')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'website/signup.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return render(request, 'website/signup.html')

        # Create a new user if validations pass
        hashed_password = make_password(password)
        user = User.objects.create(
            firstName=first_name,
            lastName=last_name,
            email=email,
            password=hashed_password,
            address=address
        )
        messages.success(request, "Account created successfully!")
        return redirect('/login/')
    return render(request, 'website/signup.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')  # Redirect to home or dashboard page
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return render(request, 'website/login.html')

    return render(request, 'website/login.html')