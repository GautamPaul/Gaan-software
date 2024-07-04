from django.urls import path
from .viewsets import IOTEventsViewSet, IOTDeviceSummary
from .views import HomeView

urlpatterns = [
    # backend
    path('', IOTEventsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('summary/<str:device>/', IOTDeviceSummary.as_view({'get': 'retrieve'})),

    # frontend
    path('home/', HomeView.as_view())
]