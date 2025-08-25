from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('add/', views.add_trip, name='add_trip'),
#     path('trips/', views.trip_list, name='trip_list'),
#     path('edit/<int:pk>/', views.edit_trip, name='edit_trip'),
#     path('delete/<int:pk>/', views.delete_trip, name='delete_trip'),
# ]
urlpatterns = [
    path('', views.user_login, name='user_login'),  # Changed default to login
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_trip, name='add_trip'),
    path('trips/', views.trip_list, name='trip_list'),
    path('edit/<int:pk>/', views.edit_trip, name='edit_trip'),
    path('delete/<int:pk>/', views.delete_trip, name='delete_trip'),
]