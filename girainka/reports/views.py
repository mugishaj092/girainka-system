from django.shortcuts import render
from django.contrib import messages
from .forms import ReportForm

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        form.user = request.user  # Associate the report with the logged-in user

        if form.is_valid():
            form.save()  # Save the report
            messages.success(request, "Your report has been submitted successfully.")
            form = ReportForm()  # Reset the form to be empty
    else:
        form = ReportForm()

    return render(request, 'website/report.html', {'form': form})
