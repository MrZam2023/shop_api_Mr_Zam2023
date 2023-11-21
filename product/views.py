from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer


@api_view(['GET'])
def product_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializer(instance=product_list, many=True).data
    return Response(data=product_list)

@api_view(['GET'])
def product_detail_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializer(instance=product_list, many=False).data
    return Response(data=product_list)

@api_view(['GET'])
def category_api_view(request):
    category_list = Product.objects.all()
    data = CategorySerializer(instance=category_list, many=True).data
    return Response(data=category_list)

@api_view(['GET'])
def category_detail_api_view(request):
    category_list = Product.objects.all()
    data = CategorySerializer(instance=category_list, many=False).data
    return Response(data=category_list)

@api_view(['GET'])
def review_api_view(request):
    review_list = Product.objects.all()
    data = ReviewSerializer(instance=review_list, many=True).data
    return Response(data=review_list)

@api_view(['GET'])
def review_detail_api_view(request):
    review_list = Product.objects.all()
    data = ReviewSerializer(instance=review_list, many=False).data
    return Response(data=review_list)

