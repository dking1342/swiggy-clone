from rest_framework.serializers import ModelSerializer
from .models import Restaurant
from ..discount.serializers import DiscountSerializer


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

    discounts = DiscountSerializer(many=False)
