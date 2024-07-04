from rest_framework.viewsets import ModelViewSet
from .models import IOTEvent
from .serializers import IOTEventSerializer


class IOTEventsViewSet(ModelViewSet):
    queryset = IOTEvent.objects.all()
    serializer_class = IOTEventSerializer