from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from .models import Customer
from django.contrib import messages
from vehicles.models import Vehicle
from bookings.models import Booking

def home(request):
    return render(request, "accounts/home.html")

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            customer = Customer.objects.get(
                email=email,
                password=password
            )

            request.session["customer_id"] = customer.id
            request.session["customer_name"] = customer.full_name

            messages.success(request, "Login Successful")

            return redirect("dashboard")

        except Customer.DoesNotExist:

            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid Email or Password"}
            )

    return render(request, "accounts/login.html")

def register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect("login")
    else:
        form = CustomerRegistrationForm()
    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )

def dashboard(request):

    if "customer_id" not in request.session:
        return redirect("login")

    customer_id = request.session["customer_id"]

    name = request.session["customer_name"]

    vehicle_count = Vehicle.objects.filter(
        customer_id=customer_id).count()

    booking_count = Booking.objects.filter(
        vehicle__customer_id=customer_id).count()

    pending_count = Booking.objects.filter(
        vehicle__customer_id=customer_id,
        status="Pending").count()

    invoice_count = booking_count
    recent_bookings = Booking.objects.filter(
    vehicle__customer_id=customer_id).order_by("-id")[:5]
    context = {
        "name": name,
        "vehicle_count": vehicle_count,
        "booking_count": booking_count,
        "pending_count": pending_count,
        "invoice_count": invoice_count,
        "recent_bookings": recent_bookings,
    }

    return render(
        request,
        "accounts/dashboard.html",
        context
    )

def logout(request):

    request.session.flush()

    return redirect("login")

