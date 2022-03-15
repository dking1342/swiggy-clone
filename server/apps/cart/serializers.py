from rest_framework.serializers import ModelSerializer
from apps.cart.models import Cart
from apps.menu.serializers import MenuSerializer


class CartSerializer(ModelSerializer):
    # order_item_name = MenuSerializer(many=False)

    class Meta:
        model = Cart
        fields = "__all__"

    # def create(self, validated_data):
    #     return Cart.objects.create(**validated_data)
