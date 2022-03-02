from django.urls import path
from . import views

app_name = "discount"

urlpatterns = [
    path("routes/", views.getRoutes, name="routes"),
    path("<uuid:pk>/", views.getDiscount, name="discount"),
    path("", views.getDiscounts, name="discounts"),
]