"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.landing, name='landing'),        # Landing page - home page for users
    path('register/', views.register, name='register'),        # Registration page - displays registration form
    path('registerdata/', views.registerdata, name='registerdata'),  # Handles registration form POST data
    path('login/', views.login, name='login'),      # Login page - displays login form
    path('logindata/', views.logindata, name='logindata'),   # Handles login form POST data
    path('dashboard/', views.dashboard, name='dashboard'),
]

