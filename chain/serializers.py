from rest_framework import serializers
from chain.models import Product, Contacts, RetailChain
from chain.validators import FactoryValidator


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RetailChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailChain
        fields = '__all__'
        read_only_fields = ('debt',)
        validators = [FactoryValidator(type='type', provider='provider')]
