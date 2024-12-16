from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

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


def message_dashboard(request):
    messages = Contact.objects.all()  # Get all messages from the database
    rows_per_page = int(request.GET.get('rows', 25))  # Get rows from query params, default to 25
    paginator = Paginator(messages, rows_per_page)  # Paginate messages list
    page_number = request.GET.get('page', 1)  # Get the current page number from query params
    page_obj = paginator.get_page(page_number)  # Get the specific page of messages
    return render(request, 'dashboard/message.html', {'page_obj': page_obj})


def get_message(request, id):
    # Get the message by ID or return 404 if not found
    message = get_object_or_404(Contact, id=id)
    
    # Prepare the message data to return
    message_data = {
        'id': str(message.id),
        'names': message.names,
        'email': message.email,
        'message': message.message,
        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Format the date
    }

    # Return the message data as JSON
    return JsonResponse({'success': True, 'message': message_data})

@csrf_exempt  # Exempt CSRF for the delete operation
def delete_message(request, id):
    if request.method == "POST":
        # Get the message by ID or return 404 if not found
        message = get_object_or_404(Contact, id=id)
        
        # Delete the message
        message.delete()
        
        # Return success response
        return JsonResponse({'success': True, 'message': 'Message deleted successfully'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)

