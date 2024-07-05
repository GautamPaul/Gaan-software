from rest_framework.serializers import ModelSerializer, DateTimeField
from .models import IOTEvent

class IOTEventSerializer(ModelSerializer):
    time = DateTimeField(format="%d-%b-%Y, %H:%M:%S", read_only=True)
    class Meta:
        model = IOTEvent
        fields = "__all__"