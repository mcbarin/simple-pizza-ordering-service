from django.db import models
from customer.models import Customer


class Flavor(models.Model):
    name = models.CharField(max_length=63, unique=True)


class Pizza(models.Model):
    count = models.PositiveIntegerField(default=0)
    flavors = models.ManyToManyField('Flavor')
    order = models.ForeignKey(
        'Order',
        blank=True,
        null=True,
        related_name='pizzas',
        on_delete=models.CASCADE
    )

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    PIZZA_SIZE_CHOICES = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )
    size = models.PositiveSmallIntegerField(
        choices=PIZZA_SIZE_CHOICES
    )


class Order(models.Model):
    information = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )

    ORDER_RECEIVED = 1
    PREPARING = 2
    COMING = 3
    DELIVERED = 4
    DELIVERY_STATUS_CHOICES = (
        (ORDER_RECEIVED, 'Order Received'),
        (PREPARING, 'Preparing'),
        (COMING, 'Coming'),
        (DELIVERED, 'Delivered'),
    )
    delivery_status = models.PositiveSmallIntegerField(
        default=ORDER_RECEIVED,
        choices=DELIVERY_STATUS_CHOICES
    )

    class Meta:
        ordering = ['id']
