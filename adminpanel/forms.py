from django import forms
from rides.models import Ride, Driver, Hospital

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = '__all__'  # Include all fields

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
