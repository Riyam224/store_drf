from django.contrib import admin

# Register your models here.
from .models import Product, Cateogory

admin.site.register(Product)
admin.site.register(Cateogory)
