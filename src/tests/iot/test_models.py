from django.test import TestCase
from iot.models import IOTEvent


class IOTEventTestCase(TestCase):
    def test_iot_event_creation(self):
        before_count = IOTEvent.objects.count()
        IOTEvent.objects.create(device="temperature", value="35", source="cloud")
        after_count = IOTEvent.objects.count()
        self.assertEqual(before_count+1, after_count)