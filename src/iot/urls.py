from django.urls import path
from .viewsets import IOTEventsViewSet
from .views import HomeView

urlpatterns = [
    # backend
    path('', IOTEventsViewSet.as_view({'get': 'list', 'post': 'create'})),

    # frontend
    path('home/', HomeView.as_view())
]