from django.db import models
from utils.models import BaseModel
from library.models import Book


class Cart(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_discount = models.IntegerField()

class InformationAboutCustomer(BaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()



