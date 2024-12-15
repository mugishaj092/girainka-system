from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def report(request):
    return render(request,'website/report.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def signup(request):
    if request.method == "POST":
        # Get data from the form
        email = request.POST.get('email')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')  # Or re-render the form with errors

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return redirect('signup')

        # Create a new user if validations pass
        hashed_password = make_password(password)
        user = User.objects.create(
            firstName=first_name,
            lastName=last_name,
            email=email,
            password=hashed_password,
            address=address
        )

        # Optional: You can log the user in automatically after signing up
        # login(request, user)

        messages.success(request, "Account created successfully!")
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'website/signup.html')

def dashboard_user(request):
    return render(request, 'dashboards/dashboard.html')