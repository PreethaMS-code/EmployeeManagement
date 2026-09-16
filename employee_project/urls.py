from django.contrib import admin
from django.urls import path, include
from employees.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('', home),
]