from rest_framework.serializers import ModelSerializer
from .models import Userinfo


class UserinfoSerializer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields = "__all__"
