from rest_framework import serializers
from customer import models


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for customer objects."""

    class Meta:
        model = models.Customer
        fields = '__all__'
