from rest_framework.serializers import ModelSerializer
from .models import Cuisines


class CuisinesSerializer(ModelSerializer):
    class Meta:
        model = Cuisines
        fields = "__all__"
