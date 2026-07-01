from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_vehicle, name="add_vehicle"),
    path("view/", views.view_vehicles, name="view_vehicles"),
    path("edit/<int:id>/", views.edit_vehicle, name="edit_vehicle"),
    path("delete/<int:id>/", views.delete_vehicle, name="delete_vehicle"),
    
]