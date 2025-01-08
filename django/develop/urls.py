from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'develop'  # This sets up URL namespacing

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]