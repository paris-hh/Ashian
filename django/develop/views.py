from django.shortcuts import render

# Create your views here.
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