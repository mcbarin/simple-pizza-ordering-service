import json

from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Flavor, Pizza, Order
from customer.models import Customer


class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data available for all tests in this class."""
        cls.customer = Customer.objects.create(
            name="Test",
            surname="User"
        )
        cls.customer2 = Customer.objects.create(
            name="Test",
            surname="User2"
        )
        cls.flavor1 = Flavor.objects.get(name='Margarita')
        cls.flavor2 = Flavor.objects.get(name='Marinara')
        cls.flavor3 = Flavor.objects.get(name='Salami')
        cls.flavor4 = Flavor.objects.get(name='Pastrami')

        cls.order = Order.objects.create(
            information="test",
            customer=cls.customer,
            delivery_status=Order.ORDER_RECEIVED
        )
        cls.order2 = Order.objects.create(
            information="test",
            customer=cls.customer2,
            delivery_status=Order.DELIVERED
        )

        cls.client = APIClient()
        cls.order_url = reverse('order-list')
        cls.order_retrieve_url = f"{cls.order_url}{cls.order.id}/"

    def test_get_order_list(self):
        response = self.client.get(self.order_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_create_order(self):
        post_data = {
                "information": "I'm allergic to Pizza",
                "customer": self.customer.id,
                "delivery_status": Order.ORDER_RECEIVED,
                "pizzas": [
                    {
                        "count": 1,
                        "flavors": [
                            self.flavor1.id,
                            self.flavor2.id
                        ],
                        "size": Pizza.SMALL
                    }
                ]
            }
        response = self.client.post(
            self.order_url,
            data=json.dumps(post_data),
            content_type="application/json"
        )
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response_json['information'],
            post_data["information"]
        )
        self.assertEqual(response_json['customer'], self.customer.id)
        self.assertEqual(
            response_json['delivery_status'],
            Order.ORDER_RECEIVED
        )
        self.assertEqual(
            response_json['pizzas'][0]['count'],
            post_data['pizzas'][0]['count']
        )
        self.assertEqual(
            response_json['pizzas'][0]['size'],
            post_data['pizzas'][0]['size']
        )
        self.assertEqual(
            response_json['pizzas'][0]['flavors'],
            post_data['pizzas'][0]['flavors']
        )

    def test_order_retrieve(self):
        response = self.client.get(
            self.order_retrieve_url,
        )
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json.get('information'),
            self.order.information
        )
        self.assertEqual(
            response_json.get('delivery_status'),
            self.order.delivery_status
        )
        self.assertEqual(
            response_json.get('customer'),
            self.order.customer.id
        )

    def test_order_update_delivery_status(self):
        response = self.client.put(
            self.order_retrieve_url,
            json.dumps({
                "customer": self.customer.id,
                "information": self.order.information,
                "delivery_status": Order.DELIVERED,
                }
            ),
            content_type="application/json"
        )
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json["delivery_status"], Order.DELIVERED)

    def test_order_update_delivery_status_delivered(self):
        self.order.delivery_status = Order.DELIVERED
        self.order.save()
        response = self.client.put(
            self.order_retrieve_url,
            json.dumps({
                "customer": self.customer.id,
                "information": self.order.information,
                "delivery_status": Order.COMING
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_order_list_filter_customer(self):
        self.order_filter_customer_url = f"{self.order_url}" + \
            f"?customer={self.customer.id}"
        response = self.client.get(
            self.order_filter_customer_url
        )
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0]['customer'], self.customer.id)

    def test_order_list_filter_delivery_status(self):
        self.order_filter_status_url = f"{self.order_url}" + \
            f"?status={Order.DELIVERED}"
        response = self.client.get(
            self.order_filter_status_url
        )
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_json), 2)

    def test_order_delete(self):
        response = self.client.delete(
            self.order_retrieve_url,
        )
        self.assertEqual(response.status_code, 204)
