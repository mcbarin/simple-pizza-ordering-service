import json

from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient


class CustomerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data available for all tests in this class."""
        cls.client = APIClient()

    def test_create_customer(self):
        url = reverse('customer-list')
        response = self.client.post(
            url,
            json.dumps({
                "name": "Cagatay",
                "surname": "Barin"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
