from rest_framework import serializers
from .models import Cart, InformationAboutCustomer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'book',
            'number_of_purchases',
            'created_at',
            'updated_at',
        )

class InformationAboutCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationAboutCustomer
        fields = (
            'id',
            'name',
            'phone_number',
            'email',
            'created_at',
            'updated_at',
        )