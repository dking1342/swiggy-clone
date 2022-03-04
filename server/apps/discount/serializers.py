from rest_framework.serializers import ModelSerializer
from .models import Discount


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"