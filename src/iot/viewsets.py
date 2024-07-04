from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import IOTEvent
from .serializers import IOTEventSerializer
from .filters import IOTEventFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse


class IOTEventsViewSet(ModelViewSet):
    queryset = IOTEvent.objects.all()
    serializer_class = IOTEventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IOTEventFilter


class IOTDeviceSummary(ViewSet):
    def retrieve(self, request, device):
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        print(from_date)
        print(to_date)
        events = IOTEvent.objects.filter(device=device)
        print(events)
        return JsonResponse({"test": "value"})