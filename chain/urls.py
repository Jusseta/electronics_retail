from django.urls import path
from rest_framework.routers import DefaultRouter
from chain.apps import ChainConfig
from chain.views import RetailChainViewSet


app_name = ChainConfig.name


router_user = DefaultRouter()
router_user.register(r'chain', RetailChainViewSet, basename='chain')

urlpatterns = [] + router_user.urls
