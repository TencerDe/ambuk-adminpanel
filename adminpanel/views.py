from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from rides.models import Driver, Hospital, Ride
from .forms import DriverForm, HospitalForm, RideForm
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('custom_admin:admin_dashboard')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'adminpanel/admin_login.html')

def admin_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('adminpanel/admin_login')
    return render(request, 'adminpanel/admin_signup.html')

def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

# Admin Dashboard
def admin_dashboard(request):
    total_rides = Ride.objects.count()
    total_drivers = Driver.objects.count()
    total_hospitals = Hospital.objects.count()
    
    context = {
        'total_rides': total_rides,
        'total_drivers': total_drivers,
        'total_hospitals': total_hospitals,
    }
    return render(request, 'adminpanel/dashboard.html', context)

# Manage Rides
def manage_rides(request):
    rides = Ride.objects.all()
    return render(request, 'adminpanel/manage_rides.html', {'rides': rides})

# Edit Ride
def edit_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if request.method == "POST":
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            return redirect('manage_rides')
    else:
        form = RideForm(instance=ride)
    return render(request, 'adminpanel/edit_ride.html', {'form': form})

# Manage Drivers
def manage_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'adminpanel/manage_drivers.html', {'drivers': drivers})

# Edit Driver
def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == "POST":
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('manage_drivers')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'adminpanel/edit_driver.html', {'form': form})

# Manage Hospitals
def manage_hospitals(request):
    hospitals = Hospital.objects.all()
    return render(request, 'adminpanel/manage_hospitals.html', {'hospitals': hospitals})

# Edit Hospital
def edit_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if request.method == "POST":
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('manage_hospitals')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'adminpanel/edit_hospital.html', {'form': form})

def delete_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if request.method == "POST":
        ride.delete()
        return redirect('manage_rides')
    return render(request, 'adminpanel/delete_confirm.html', {'ride': ride})

def delete_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if request.method == "POST":
        hospital.delete()
        return redirect('manage_hospitals')
    return render(request, 'adminpanel/delete_confirm.html', {'object': hospital, 'type': 'Hospital'})

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == "POST":
        driver.delete()
        return redirect('custom_admin:manage_drivers')
    return render(request, 'adminpanel/delete_confirm.html', {'object': driver, 'type': 'Driver'})

def add_driver(request):
    if request.method == "POST":
        name = request.POST.get("name") 
        phone = request.POST.get("phone")  
        is_available = request.POST.get("is_available") == "on"
        
        if not phone:
            return HttpResponse("Phone number is required", status=400)

        Driver.objects.create(name=name, phone=phone, is_available=is_available)
        return redirect("custom_admin:manage_drivers")

    return render(request, "adminpanel/add_driver.html")

def add_hospital(request):
    if request.method == "POST":
        name = request.POST.get("name")
        location = request.POST.get('Location')
        if name and location:
            Hospital.objects.create(name=name, location=location)
            messages.success(request, "Hospital added successfully!")
            return redirect ('manage_hospitals')
        else:
            messages.error(request, "All fields are required")
    return render(request,'adminpanel/add_hospital.html')

def add_ride(request):
    if request.method == "POST":
        name = request.POST.get("name")
        status = request.POST.get('status')
        if name and status:
            Ride.objects.create(name=name, status=status)
            messages.success(request, "Ride added successfully!")
            return redirect ('manage_rides')
        else:
            messages.error(request, "All fields are required")
    return render(request,'adminpanel/add_ride.html')
