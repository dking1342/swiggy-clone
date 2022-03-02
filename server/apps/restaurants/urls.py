from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("routes/", views.getRoutes, name="routes"),
    path("<uuid:pk>/", views.getRestaurant, name="restaurant"),
    path("", views.getRestaurants, name="restaurants"),
]
