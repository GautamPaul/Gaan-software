from django.urls import path
from .viewsets import IOTEventsViewSet, IOTDeviceSummary
from .views import HomeView, QueryView, SummaryView

urlpatterns = [
    # backend
    path('', IOTEventsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('summary/<str:device>/', IOTDeviceSummary.as_view({'get': 'retrieve'})),

    # frontend
    path('home/', HomeView.as_view(), name="home"),
    path('query/', QueryView.as_view(), name="query"),
    path('summary/', SummaryView.as_view(), name="summary"),
]