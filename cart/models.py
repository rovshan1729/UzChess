from django.db import models
from utils.models import BaseModel
from library.models import Book
from django.utils.text import slugify


class Cart(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    number_of_purchases = models.IntegerField(default=1)
    
class InformationAboutCustomer(BaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name