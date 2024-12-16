from django.shortcuts import render
from django.contrib import messages
from .forms import ReportForm
from .models import Report
from django.core.paginator import Paginator
from django.http import JsonResponse

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        form.user = request.user  # Associate the report with the logged-in user

        if form.is_valid():
            form.save()  # Save the report
            messages.success(request, "Your report has been submitted successfully.")
            form = ReportForm()  
    else:
        form = ReportForm()

    return render(request, 'website/report.html', {'form': form})


def report_dashboard(request):
    reports = Report.objects.all()
    paginator = Paginator(reports, 10)  # Paginate with 10 reports per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/report.html', {'page_obj': page_obj})

def get_report(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
        data = {
            'success': True,
            'report': {
                'full_name': report.full_name,
                'email': report.email,
                'message': report.message,
                'address': report.address,
                'phone': report.phone,
                'created_at': report.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
        }
    except Report.DoesNotExist:
        data = {'success': False, 'message': 'Report not found.'}

    return JsonResponse(data)

def delete_report(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
        report.delete()
        data = {'success': True, 'message': 'Report deleted successfully.'}
    except Report.DoesNotExist:
        data = {'success': False, 'message': 'Report not found.'}
    
    return JsonResponse(data)