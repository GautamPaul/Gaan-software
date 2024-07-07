from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from iot.models import IOTEvent
from iot.viewsets import IOTEventsViewSet


class IOTEventsViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        IOTEvent.objects.create(device="temperature", value="35", source="cloud")
        IOTEvent.objects.create(device="speed", value="65", source="cloud")
        
    
    def test_get_iot_events(self):
        url = "/iot/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_filter_iot_events(self):
        url = "/iot/?device=temperature"
        filtered_response = len(self.client.get(url).json().get("results"))
        self.assertEqual(filtered_response, 1)
    
    def test_create_iot_event(self):
        before_count = IOTEvent.objects.count()
        post_data = {
            "device": "test_device",
            "value": 10,
            "source": "some_source"
        }
        url = "/iot/"
        created_event = self.client.post(url, post_data)
        after_count = IOTEvent.objects.count()
        self.assertEqual(before_count+1, after_count)

