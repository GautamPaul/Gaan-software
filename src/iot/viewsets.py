from rest_framework.viewsets import ModelViewSet
from .models import IOTEvent
from .serializers import IOTEventSerializer


class IOTEventsView(ModelViewSet):
    queryset = IOTEvent.objets.all()
    serializer_class = IOTEventSerializer