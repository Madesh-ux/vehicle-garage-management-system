from django.shortcuts import render, redirect
from .forms import VehicleForm
from .models import Vehicle
from django.contrib import messages

def add_vehicle(request):

    if request.method == "POST":

        form = VehicleForm(request.POST)

        if form.is_valid():

            vehicle = form.save(commit=False)

            vehicle.customer_id = request.session["customer_id"]

            vehicle.save()

            messages.success(request, "Vehicle Added Successfully")

            return redirect("dashboard")

    else:

        form = VehicleForm()

    return render(request, "vehicles/add_vehicle.html", {"form": form})

def view_vehicles(request):

    customer_id = request.session["customer_id"]

    vehicles = Vehicle.objects.filter(customer_id=customer_id)

    return render(
        request,
        "vehicles/view_vehicles.html",
        {"vehicles": vehicles}
    )

def edit_vehicle(request, id):

    customer_id = request.session["customer_id"]

    vehicle = Vehicle.objects.get(
    id=id,
    customer_id=customer_id
    )

    if request.method == "POST":

        form = VehicleForm(request.POST, instance=vehicle)

        if form.is_valid():

            form.save()

            messages.success(request, "Vehicle Updated Successfully")

            return redirect("view_vehicles")

    else:

        form = VehicleForm(instance=vehicle)

    return render(
        request,
        "vehicles/edit_vehicle.html",
        {"form": form}
    )

def delete_vehicle(request, id):

    customer_id = request.session["customer_id"]

    vehicle = Vehicle.objects.get(
    id=id,
    customer_id=customer_id
    )

    vehicle.delete()

    messages.success(request, "Vehicle Deleted Successfully")

    return redirect("view_vehicles")