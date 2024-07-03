from rest_framework.viewsets import ModelViewSet
from .models import IOTEvent


class IOTEventsView(ModelViewSet):
    queryset = IOTEvent.objets.all()