from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'develop/homepage.html')

def about(request):
    return render(request, 'develop/about.html')

def contact(request):
    return render(request, 'develop/contact.html')

def login(request):
    return render(request, 'develop/login.html')

def privacy(request):
    return render(request, 'develop/privacy.html')

def terms(request):
    return render(request, 'develop/terms.html')