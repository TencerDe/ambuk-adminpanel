from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('custom-admin/', include('adminpanel.urls'))
]
