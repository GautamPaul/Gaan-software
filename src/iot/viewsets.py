from rest_framework.viewsets import ModelViewSet
from .models import IOTEvent
from .serializers import IOTEventSerializer
from .filters import IOTEventFilter
from django_filters import rest_framework as filters


class IOTEventsViewSet(ModelViewSet):
    queryset = IOTEvent.objects.all()
    serializer_class = IOTEventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = IOTEventFilter