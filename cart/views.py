from .serializers import CartSerializer, InformationAboutCustomerSerializer
from .models import Cart, InformationAboutCustomer
from rest_framework import generics

class CartAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class InformationAboutCustomerAPIView(generics.ListAPIView):
    queryset = InformationAboutCustomer.objects.all()
    serializer_class = InformationAboutCustomerSerializer
