from django_filters import rest_framework as filters
from .models import IOTEvent

class IOTEventFilter(filters.FilterSet):
    class Meta:
        model = IOTEvent
        fields = ["device", "time"]
