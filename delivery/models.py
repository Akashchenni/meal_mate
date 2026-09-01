from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length= 20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

class Restaurent(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField(max_length=200,default="https://png.pngtree.com/png-vector/20250910/ourmid/pngtree-restaurant-logo-with-chef-hat-and-fork-spoon-symbol-png-image_17398231.webp")
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurent, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    picture = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    is_veg = models.BooleanField(default=True)