from django.urls import path
from . import views

app_name = "userinfo"

urlpatterns = [
    path("routes/", views.getRoutes, name="routes"),
    path("<uuid:pk>/", views.getUserinfo, name="user"),
    path("", views.getUserinfos, name="users"),
]
