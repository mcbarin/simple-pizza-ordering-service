from django.shortcuts import render
from django.core.exceptions import ValidationError

from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import APIException
from rest_framework.serializers import ValidationError

from customer import models, serializers


class CustomerBaseViewSet(viewsets.GenericViewSet):
    """Customer base view set with basic attributes"""
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerCreateListViewSet(CustomerBaseViewSet,
                                mixins.CreateModelMixin,
                                mixins.ListModelMixin):
    """Customer create, list view sets"""
    pass
