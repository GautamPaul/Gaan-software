from django.urls import path
from .viewsets import IOTEventsViewSet

urlpatterns = [
    path('', IOTEventsViewSet.as_view({'get': 'list'})),
]