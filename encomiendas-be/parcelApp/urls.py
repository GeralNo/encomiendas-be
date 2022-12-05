from django.urls import path
from parcelApp import views
 
urlpatterns = [
    path('', views.EnviosListCreateView.as_view()),    
    path('<int:pk>/', views.EnviosDetailView.as_view()), 
    path('', views.TrabajadoresListCreateView.as_view()),    
    path('<int:pk>/', views.TrabajadoresDetailView.as_view()), 
    path('', views.TransportadoresListCreateView.as_view()),    
    path('<int:pk>/', views.TransportadoresDetailView.as_view()), 

]
