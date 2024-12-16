from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .models import User
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator


def restrict_logged_in_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
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

        if not first_name or not last_name:
            messages.error(request, "First name and last name are required!")
            return render(request, 'website/signup.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'website/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return render(request, 'website/signup.html')

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

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return render(request, 'website/login.html')

    return render(request, 'website/login.html')

def user_dashboard(request):
    users = User.objects.all()
    rows_per_page = int(request.GET.get('rows', 25))  # Get rows from query params, default to 25
    paginator = Paginator(users, rows_per_page)  # Dynamic rows per page
    page_number = request.GET.get('page', 1)  # Get current page number from query params
    page_obj = paginator.get_page(page_number)  # Get the specific page
    return render(request, 'dashboard/users.html', {'page_obj': page_obj})


def delete_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return JsonResponse({"success": True, "message": "User deleted successfully."})
    return JsonResponse({"success": False, "message": "Invalid request."}, status=400)

def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = {
            'success': True,
            'user': {
                'email': user.email,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'address': user.address,
                'role': user.get_role_display(),
                'verified': user.verified,
                'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
        }
    except User.DoesNotExist:
        data = {'success': False, 'message': 'User not found.'}

    return JsonResponse(data)