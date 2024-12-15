from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from cows.models import Cow
from reports.models import Report
import json

User = get_user_model() 

# Website views
def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def report(request):
    return render(request, 'website/report.html')

def contact(request):
    return render(request, 'website/contact.html')

# Signup view
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
        try:
            user = User.objects.create_user(
                email=email,
                password=password,
                firstName=first_name,
                lastName=last_name,
                address=address
            )
            messages.success(request, "Account created successfully!")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')

    return render(request, 'website/signup.html')

def dashboard(request):
    from datetime import timedelta
    from django.utils import timezone

    total_users = User.objects.count()
    total_cows = Cow.objects.count()
    total_reports = Report.objects.count()

    thirty_days_ago = timezone.now() - timedelta(days=30)
    active_users = User.objects.filter(last_login__gte=thirty_days_ago).count()

    report_trends = Report.objects.annotate(
        month=ExtractMonth('created_at')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    report_counts = {str(i): 0 for i in range(1, 13)} 
    for trend in report_trends:
        report_counts[str(trend['month'])] = trend['count']

    context = {
        'total_users': total_users,
        'total_cows': total_cows,
        'total_reports': total_reports,
        'active_users': active_users,
        'report_counts': json.dumps(report_counts), 
    }
    return render(request, 'dashboard/dashboard.html', context)