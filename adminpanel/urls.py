from django.urls import path
from .views import (
    admin_dashboard, manage_rides, manage_drivers, manage_hospitals,
    edit_ride, edit_driver, edit_hospital, delete_ride, delete_driver, delete_hospital,
    add_ride, add_driver, add_hospital, admin_login, admin_signup
)

# ✅ Add this line to define the app namespace
app_name = "custom_admin"  

urlpatterns = [
    path('login/', admin_login, name='admin_login'),
    path('signup/', admin_signup, name='admin_signup'),
    path('dashboard', admin_dashboard, name='admin_dashboard'),
    
    # Ride URLs
    path('custom-admin/rides/', manage_rides, name='manage_rides'),
    path('custom-admin/rides/add/', add_ride, name='add_ride'),
    path('custom-admin/rides/edit/<int:ride_id>/', edit_ride, name='edit_ride'),
    path('custom-admin/rides/delete/<int:ride_id>/', delete_ride, name='delete_ride'),
    
    # Driver URLs
    path('custom-admin/drivers/', manage_drivers, name='manage_drivers'),
    path('custom-admin/drivers/add/', add_driver, name='add_driver'),
    path('custom-admin/drivers/edit/<int:driver_id>/', edit_driver, name='edit_driver'),
    path('custom-admin/drivers/delete/<int:driver_id>/', delete_driver, name='delete_driver'),

    # Hospital URLs
    path('custom-admin/hospitals/', manage_hospitals, name='manage_hospitals'),
    path('custom-admin/hospitals/add/', add_hospital, name='add_hospital'),
    path('custom-admin/hospitals/edit/<int:hospital_id>/', edit_hospital, name='edit_hospital'),
    path('custom-admin/hospitals/delete/<int:hospital_id>/', delete_hospital, name='delete_hospital'),
]