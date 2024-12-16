from django.shortcuts import redirect
from django.urls import reverse

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define public and restricted paths
        public_paths = [reverse('login'), reverse('signup'), reverse('about'), reverse('contact'), reverse('home')]

        restricted_paths = [reverse('report'), reverse('dashboard'), reverse('cow'), reverse('users'), reverse('report_dashboard')]

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # If the user is logged in but trying to access login or signup, redirect to home
            if request.path in [reverse('login'), reverse('signup')]:
                return redirect('home')

            # Check if the user is an admin (assuming the role is stored in request.user.role)
            if request.user.role == 'admin' and request.path in restricted_paths:
                # Admins can access the dashboard
                return self.get_response(request)
            
            # If the user is a citizen and trying to access restricted paths like the dashboard, redirect to home
            elif request.user.role == 'citizen' and request.path in restricted_paths:
                return redirect('home')

        # If the user is not authenticated and trying to access restricted pages, redirect to login
        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect('login')

        response = self.get_response(request)
        return response
