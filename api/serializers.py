from rest_framework import serializers
from api import models
from drf_writable_nested.serializers import WritableNestedModelSerializer


class FlavorSerializer(serializers.ModelSerializer):
    """Serializer for flavor objects"""

    class Meta:
        model = models.Flavor
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    """Serializer for pizza objects."""

    class Meta:
        model = models.Pizza
        fields = (
            'id',
            'count',
            'flavors',
            'size',
        )


class OrderSerializer(WritableNestedModelSerializer):
    """Serializer for order objects"""
    pizzas = PizzaSerializer(many=True, required=False)

    class Meta:
        model = models.Order
        fields = (
            'id',
            'information',
            'customer',
            'delivery_status',
            'pizzas',
        )
        read_only_fields = ('id',)
