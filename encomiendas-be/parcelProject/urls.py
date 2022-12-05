"""parcelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from parcelApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/', views.EnviosListCreateView.as_view()),
    path('user/<int:pk>/', views.EnviosDetailView.as_view()),
    path('user/', views.TrabajadoresListCreateView.as_view()),
    path('user/<int:pk>/', views.TrabajadoresDetailView.as_view()),
    path('user/', views.TransportadoresListCreateView.as_view()),
    path('user/<int:pk>/', views.TransportadoresDetailView.as_view()),
    path('envios/', include('parcelApp.urls')),
    path('trabajadores/', include('parcelApp.urls')),
    path('transportadores/', include('parcelApp.urls')),
]