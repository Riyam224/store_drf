from rest_framework import serializers
from .models import Product, Cateogory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cateogory
        fields = "__all__"
