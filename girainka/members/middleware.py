from django.shortcuts import redirect
from django.urls import reverse

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_paths = [reverse('login'), reverse('signup'), reverse('about'), reverse('contact'), reverse('home')]

        restricted_paths = [reverse('report')]  # Add 'dashboard' URL here

        if request.user.is_authenticated and request.path in [reverse('login'), reverse('signup')]:
            return redirect('home')

        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect('login')

        response = self.get_response(request)
        return response
