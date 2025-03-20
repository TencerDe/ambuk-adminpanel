from django.db import models

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
    
class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Ride(models.Model):
    AMBULANCE_TYPES = [
        ('basic','Basic ambulance'),
        ('medical','Ambulance with medical assistance'),
    ]

    VEHICLE_TYPES = [
        ('van','Van'),
        ('minibus', 'Minibus'),
        ('traveller','Traveller'),
    ]

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    ambulance_type = models.CharField(choices=AMBULANCE_TYPES, max_length=10)
    vehicle_type = models.CharField(choices=VEHICLE_TYPES, max_length=10)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True) 
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"Ride for {self.name} to {self.hospital.name}"
