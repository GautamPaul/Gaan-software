import requests

from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        response = requests.get("http://127.0.0.1:8000/iot/")
        iot_events = response.json().get("results")
        return render(request, "home.html", {"iot_events": iot_events})

class QueryView(View):
    def get(self, request):
        print(request.GET)
        if request.GET:
            device=request.GET.get("device", "")
            from_date = request.GET.get("from_date", "")
            to_date = request.GET.get("to_date", "")
            url = f"http://127.0.0.1:8000/iot/?device={device}&from_date={from_date}&to_date={to_date}"
            response = requests.get(url)
            iot_events = response.json().get("results")
            return render(request, "filter.html", {"iot_events": iot_events})
        else:
            return render(request, "filter.html")

class SummaryView(View):
    def get(self, request):
        return render(request, "summary.html")