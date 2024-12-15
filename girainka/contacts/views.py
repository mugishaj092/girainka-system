from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        names = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not names or not email or not message:
            messages.error(request, 'All fields are required!')
            return redirect('contact')

        try:
            contact_entry = Contact.objects.create(
                names=names,
                email=email,
                message=message
            )
            contact_entry.save()
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('contact')

        return redirect('contact')

    return render(request, 'website/contact.html')
