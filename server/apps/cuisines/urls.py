from django.urls import path
from . import views

app_name = "cuisines"

urlpatterns = [
    path("routes/", views.getRoutes,name="routes"),
    path("<uuid:pk>/", views.getCuisine, name="cuisine"),
    path("", views.getCuisines, name="cuisines")
]