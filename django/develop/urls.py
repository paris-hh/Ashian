from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'develop'  # This sets up URL namespacing

urlpatterns = [
    path('', views.homepage, name='home'),
    path('index/', views.indexpage, name='index'),
    path('index1/', views.indexpage1, name='index1'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]