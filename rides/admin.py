from django.contrib import admin
from .models import Hospital, Driver, Ride

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Driver)
admin.site.register(Ride)
