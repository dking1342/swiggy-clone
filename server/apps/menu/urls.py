from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("routes/", views.get_routes, name="routes"),
    path("restaurant/<uuid:pk>/", views.get_menu_restaurant, name="menu_restaurant"),
    path("<uuid:pk>/", views.get_menu, name="menu"),
    path("", views.get_menus, name="menus"),
]