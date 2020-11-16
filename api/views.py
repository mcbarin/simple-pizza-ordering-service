from django.shortcuts import render
from django.core.exceptions import ValidationError

from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import APIException
from rest_framework.serializers import ValidationError

from django_filters.rest_framework import DjangoFilterBackend

from api import models, serializers


class FlavorBaseViewSet(viewsets.GenericViewSet):
    """Flavor base view set with basic attributes"""
    queryset = models.Flavor.objects.all()
    serializer_class = serializers.FlavorSerializer


class FlavorCreateListViewSet(FlavorBaseViewSet,
                              mixins.CreateModelMixin,
                              mixins.ListModelMixin):
    """Flavor create, list view sets"""
    pass


class OrderBaseViewSet(viewsets.GenericViewSet):
    """Order base view set with basic attributes"""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderCreateListViewSet(OrderBaseViewSet,
                             mixins.CreateModelMixin,
                             mixins.ListModelMixin):
    """Order create, list view sets"""
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['delivery_status', 'customer']


class OrderRetrieveUpdateDestroyViewSet(OrderBaseViewSet,
                                        mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin,
                                        mixins.DestroyModelMixin):
    """Order retrieve, update, destroy view sets"""

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.delivery_status == models.Order.DELIVERED:
            # raise APIException("Can't update order object.")
            raise ValidationError(
                "Order object can't be updated" +
                " when delivery_status = " +
                instance.get_delivery_status_display()
            )
        else:
            serializer.save()
