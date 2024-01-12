from rest_framework import viewsets
from chain.models import RetailChain, Contacts, Product
from chain.serializers import RetailChainSerializer, ContactSerializer, ProductSerializer
from users.permissions import IsActive


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class RetailChainViewSet(viewsets.ModelViewSet):
    queryset = RetailChain.objects.all()
    serializer_class = RetailChainSerializer
    permission_classes = [IsActive]
