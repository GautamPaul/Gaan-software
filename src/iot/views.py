import requests

from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        response = requests.get("http://127.0.0.1:8000/iot/")
        iot_events = response.json().get("results")
        return render(request, "home.html", {"iot_events": iot_events})