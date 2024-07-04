from django_filters import rest_framework as filters
from .models import IOTEvent

class IOTEventFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="time", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="time", lookup_expr="lte")
    class Meta:
        model = IOTEvent
        fields = ["device"]
