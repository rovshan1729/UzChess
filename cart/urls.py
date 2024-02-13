from django.urls import path
from .views import CartAPIView, InformationAboutCustomerAPIView

urlpatterns = [
    path('cart/', CartAPIView.as_view()),
    path('info/', InformationAboutCustomerAPIView.as_view())
]