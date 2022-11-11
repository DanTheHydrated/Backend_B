from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import Menu

# Create your views here.

def get_menu(request):
    data = [i.json() for i in Menu.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")
