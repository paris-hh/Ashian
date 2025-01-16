from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError

def health_check(request):
    db_health = "ok"
    try:
        connection = connections['default']
        connection.cursor()
    except OperationalError:
        db_health = "unavailable"

    return JsonResponse({"status": "ok", "database": db_health}, status=200 if db_health == "ok" else 500)

def homepage(request):
    return render(request, 'develop/homepage.html')

def indexpage(request):

    context = {
        'message': 'Hello, Django!',
    }

    return render(request, 'develop/index.html', context)

def indexpage1(request):

    context = {
        'message': 'Hello, Django!',
    }

    return render(request, 'develop/index1.html', context)

def about(request):
    return render(request, 'develop/about.html')

def contact(request):
    return render(request, 'develop/contact.html')

def login(request):
    return render(request, 'develop/login.html')

def register(request):
    return render(request, 'develop/register.html')

def privacy(request):
    return render(request, 'develop/privacy.html')

def terms(request):
    return render(request, 'develop/terms.html')