from django_filters.rest_framework import FilterSet, DateFilter
from .models import IOTEvent

class IOTEventFilter(FilterSet):
    from_date = DateFilter(field_name="time", lookup_expr="gte")
    to_date = DateFilter(field_name="time", lookup_expr="lte")
    class Meta:
        model = IOTEvent
        fields = ["device"]
