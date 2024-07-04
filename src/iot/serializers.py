from rest_framework.serializers import ModelSerializer
from .models import IOTEvent

class IOTEventSerializer(ModelSerializer):
    class Meta:
        model = IOTEvent
        fields = "__all__"