from django.contrib import admin
from ishoppers.models import OrderHistory, Person, Product

# Register your models here.

admin.site.register(OrderHistory)
admin.site.register(Person)
admin.site.register(Product)