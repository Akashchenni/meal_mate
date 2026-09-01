from django.contrib import admin
from .models import Customer,Restaurent, Item

# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurent)
admin.site.register(Item)
