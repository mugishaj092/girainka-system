from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def report(request):
    return render(request,'website/report.html')
def contact(request):
    return render(request, 'contact.html')

def users(request):
    return render(request, 'website/users.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup') 

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return redirect('signup')

        hashed_password = make_password(password)
        user = User.objects.create(
            firstName=first_name,
            lastName=last_name,
            email=email,
            password=hashed_password,
            address=address
        )


        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'website/signup.html')
