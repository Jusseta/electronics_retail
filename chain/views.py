from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from chain.models import RetailChain, Contacts, Product
from chain.paginators import RetailChainPaginator
from chain.serializers import RetailChainSerializer, ContactSerializer, ProductSerializer
from users.permissions import UserIsActive


class ContactsViewSet(viewsets.ModelViewSet):
    """ViewSet for contacts"""
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [UserIsActive]
    pagination_class = RetailChainPaginator
    filter_backends = [SearchFilter]
    search_fields = ['country']


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [UserIsActive]
    pagination_class = RetailChainPaginator


class RetailChainViewSet(viewsets.ModelViewSet):
    """ViewSet for retail chain"""
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainSerializer
    permission_classes = [UserIsActive]
    pagination_class = RetailChainPaginator
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']
