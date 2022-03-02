from rest_framework.serializers import ModelSerializer
from .models import Menu


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
