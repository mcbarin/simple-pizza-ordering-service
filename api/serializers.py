from rest_framework import serializers
from api import models
from drf_writable_nested.serializers import WritableNestedModelSerializer


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
    pizzas = PizzaSerializer(many=True)

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

    # def create(self, validated_data):
    #     pizzas_data = validated_data.pop('pizzas')
    #     order = models.Order.objects.create(**validated_data)

    #     # Also create pizza objects.
    #     for pizza in pizzas_data:
    #         flavors = pizza.pop('flavors')
    #         pizza_object = models.Pizza.objects.create(order=order, **pizza)

    #         flavors_id_list = [flavor.id for flavor in flavors]
    #         for flavor in flavors_id_list:
    #             pizza_object.flavors.add(flavor)
    #     return order

        
