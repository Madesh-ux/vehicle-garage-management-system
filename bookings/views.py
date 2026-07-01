from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
from vehicles.models import Vehicle

def book_service(request):

    if "customer_id" not in request.session:
        return redirect("login")

    customer_id = request.session["customer_id"]

    if request.method == "POST":

        form = BookingForm(request.POST)

        form.fields["vehicle"].queryset = Vehicle.objects.filter(
            customer_id=customer_id
        )

        if form.is_valid():

            form.save()

            messages.success(request, "Service Booked Successfully")

            return redirect("dashboard")

    else:

        form = BookingForm()

        form.fields["vehicle"].queryset = Vehicle.objects.filter(
            customer_id=customer_id
        )

    return render(
        request,
        "bookings/book_service.html",
        {"form": form}
    )

def view_bookings(request):

    customer_id = request.session["customer_id"]

    bookings = Booking.objects.filter(
        vehicle__customer_id=customer_id
    )

    return render(
        request,
        "bookings/view_bookings.html",
        {"bookings": bookings}
    )

def cancel_booking(request, id):

    booking = Booking.objects.get(id=id)

    booking.delete()

    return redirect("view_bookings")
def invoice(request, id):

    if "customer_id" not in request.session:
        return redirect("login")

    customer_id = request.session["customer_id"]

    booking = Booking.objects.get(
        id=id,
        vehicle__customer_id=customer_id
    )

    return render(
        request,
        "bookings/invoice.html",
        {"booking": booking}
    )