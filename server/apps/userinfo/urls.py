from django.urls import path
from . import views

app_name = "userinfo"

urlpatterns = [
    path("routes/", views.getRoutes, name="routes"),
    path("get/<str:pk>/", views.get_user_info, name="user"),
    path("create/", views.create_user, name="create_user"),
    path("", views.get_users_info, name="users"),
]
