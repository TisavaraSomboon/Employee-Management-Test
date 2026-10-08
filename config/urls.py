from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),  # Includes all DRF routes
    path('api-auth/', include('rest_framework.urls')),  # Enables login UI in DRF browser view
]