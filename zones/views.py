from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import read_zones, create_zone, delete_zone

@csrf_exempt
def fetch_zones(request):
    if request.method == 'GET':
        zones = read_zones()
        return JsonResponse(zones, safe=False)
    return HttpResponse(status=405)  # Method Not Allowed

@csrf_exempt
def create_zone_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            points = data['points']
            created_zone = create_zone(name, points)
            return JsonResponse(created_zone, status=201)  # Created
        except (KeyError, json.JSONDecodeError):
            return HttpResponse(status=400)  # Bad Request
    return HttpResponse(status=405)  # Method Not Allowed

@csrf_exempt
def delete_zone_view(request, zone_id):
    if request.method == 'DELETE':
        delete_zone(zone_id)
        return HttpResponse(status=204)  # No Content
    return HttpResponse(status=405)  # Method Not Allowed
