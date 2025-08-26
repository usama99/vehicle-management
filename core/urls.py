from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('logistics.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logistics.urls')),      # '' → login view inside logistics.urls
]