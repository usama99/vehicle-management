from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_trip, name='add_trip'),
    path('trips/', views.trip_list, name='trip_list'),
    path('edit/<int:pk>/', views.edit_trip, name='edit_trip'),
    path('delete/<int:pk>/', views.delete_trip, name='delete_trip'),
]