from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from customer import views as customer_views

router = DefaultRouter()

router.register('flavor', views.FlavorCreateListViewSet)

router.register('order', views.OrderCreateListViewSet)
router.register('order', views.OrderRetrieveUpdateDestroyViewSet)

router.register('customer', customer_views.CustomerCreateListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
