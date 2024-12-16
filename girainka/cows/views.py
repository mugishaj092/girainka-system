from django.http import JsonResponse
from .models import Cow,Source
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from members.models import User

def get_cow(request, cow_id):
    try:
        cow = Cow.objects.get(id=cow_id)
        data = {
            "success": True,
            "cow": {
                "name": cow.name,
                "owner": str(cow.owner),
                "status": cow.status,
                "reason": cow.reason,
                "birthdate": cow.birthdate,
                "created_at": cow.created_at,
            }
        }
    except Cow.DoesNotExist:
        data = {"success": False, "message": "Cow not found."}
    return JsonResponse(data)

def delete_cow(request, cow_id):
    try:
        cow = Cow.objects.get(id=cow_id)
        cow.delete()
        return JsonResponse({"success": True, "message": "Cow deleted successfully."})
    except Cow.DoesNotExist:
        return JsonResponse({"success": False, "message": "Cow not found."})
    
def cow_dashboard(request):
    cows = Cow.objects.all()
    rows_per_page = int(request.GET.get('rows', 25))
    paginator = Paginator(cows, rows_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    users_without_cows = User.objects.exclude(id__in=Cow.objects.values('owner'))    
    # Get all sources
    sources = Source.objects.all()

    # Debug print statements
    print(users_without_cows)
    print(sources)
    print("Success=======================")
    return render(request, 'dashboard/cow.html', {'page_obj': page_obj,'users': users_without_cows, 'sources': sources})


def get_source(request, source_id):
    try:
        source = Source.objects.get(id=source_id)
        data = {
            "success": True,
            "source": {
                "province": source.province,
                "district": source.district,
                "sector": source.sector,
                "cell": source.cell,
                "village": source.village,
                "created_at": source.created_at,
            }
        }
    except Source.DoesNotExist:
        data = {"success": False, "message": "Source not found."}
    return JsonResponse(data)

# View to delete a specific source
def delete_source(request, source_id):
    try:
        source = Source.objects.get(id=source_id)
        source.delete()
        return JsonResponse({"success": True, "message": "Source deleted successfully."})
    except Source.DoesNotExist:
        return JsonResponse({"success": False, "message": "Source not found."})

# View to display the source dashboard with pagination
def source_dashboard(request):
    sources = Source.objects.all()
    rows_per_page = int(request.GET.get('rows', 25))
    paginator = Paginator(sources, rows_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/source.html', {'page_obj': page_obj})

def add_cow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        owner_id = data.get("owner")
        status = data.get("status")
        reason = data.get("reason")
        birthdate = data.get("birthdate")
        source_id = data.get("source")
        
        try:
            # Find the Source and Owner
            source = Source.objects.get(id=source_id)
            owner = User.objects.get(id=owner_id)
            
            # Create the Cow object
            cow = Cow.objects.create(
                name=name,
                owner=owner,
                status=status,
                reason=reason,
                birthdate=birthdate,
                source=source
            )
            print(source)
            print(owner)
            return JsonResponse({"success": True, "message": "Cow added successfully."})
        except Source.DoesNotExist:
            return JsonResponse({"success": False, "message": "Source not found."})
        except User.DoesNotExist:
            return JsonResponse({"success": False, "message": "Owner not found."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    else:
        users = User.objects.all()  # Get all users to populate the owner dropdown
        print(users)
        print("Success=======================")
        sources = Source.objects.all()  # Get all sources for the source dropdown
        return render(request, 'dashboard/cow.html', {'users': users, 'sources': sources})
