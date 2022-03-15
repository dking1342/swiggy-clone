from django.urls import path
from . import views

app_name = "rating"

urlpatterns = [
    path("routes/", views.get_routes, name="routes"),
    path("get/<uuid:pk>/", views.get_rating, name="rating"),
    path("create/", views.create_rating, name="create_rating"),
    path("list/", views.get_ratings, name="ratings")
]