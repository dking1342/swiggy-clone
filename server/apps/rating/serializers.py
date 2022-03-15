from rest_framework.serializers import ModelSerializer
from apps.rating.models import Rating

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"