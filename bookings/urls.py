from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_service, name="book_service"),
    path("view/", views.view_bookings, name="view_bookings"),
    path("cancel/<int:id>/", views.cancel_booking, name="cancel_booking"),
    path("invoice/<int:id>/", views.invoice, name="invoice"),
    
]