from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("routes/", views.get_routes, name="routes"),
    path("get/<uuid:pk>/", views.get_order, name="cart"),
    path("create/", views.create_order, name="create_cart"),
    path("", views.get_orders, name="cart")
]