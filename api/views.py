from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product, Cateogory
from .serializers import *
from rest_framework.decorators import api_view

from rest_framework.response import Response


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def add_product(request):
    serializeData = ProductSerializer(data=request.data)
    if serializeData.is_valid():
        serializeData.save()
    return Response(serializeData.data)


@api_view(["PUT"])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
