from rest_framework.serializers import ModelSerializer
from .models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
