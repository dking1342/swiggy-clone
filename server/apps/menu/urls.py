from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("routes/", views.getRoutes, name="routes"),
    path("<uuid:pk>/", views.getMenu, name="menu"),
    path("", views.getMenus, name="menus"),
]