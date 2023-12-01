from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review, Tag
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer, TagSerializer, ProductValidateSerializer, CategoryValidateSerializer, ReviewValidateSerializer, TagValidateSerializer


@api_view(['GET', 'POST'])
def product_api_view(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        data = ProductSerializer(instance=product_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

        product = Product.objects.create(
            title=title, description=description, price=price, category_id=category_id
        )
        return Response(data={'product_id': product.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    if request.method == 'GET':
        product_list = Product.objects.all()
        data = ProductSerializer(instance=product_list, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = ProductValidateSerializer
        serializer.is_valid(raise_exception=True)
        product_detail_api_view.title = request.data.get('title')
        product_detail_api_view.description = request.data.get('description')
        product_detail_api_view.price = request.data.get('price')
        product_detail_api_view.category_id = request.data.get('category_id')


        return Response(data={'product_id': product_detail_api_view.id}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        product_detail_api_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def category_api_view(request):
    if request.method == 'GET':
        serializer = CategoryValidateSerializer
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        category_list = Category.objects.all()
        data = CategorySerializer(instance=category_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(
            name=name
        )
        return Response(data={'category_id': category.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request,id):
    if request.method == 'GET':
        category_list = Category.objects.all()
        data = CategorySerializer(instance=category_list, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = CategoryValidateSerializer
        serializer.is_valid(raise_exception=True)
        category_detail_api_view.name = request.data.get('name')
        return Response(data={'category_id': category_detail_api_view.id}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        category_detail_api_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_api_view(request):
    if request.method == 'GET':
        review_list = Product.objects.all()
        data = ReviewSerializer(instance=review_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')

        review = Review.objects.create(
            text=text, stars=stars, product_id=product_id
        )
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request):
    if request.method == 'GET':
        review_list = Product.objects.all()
        data = ReviewSerializer(instance=review_list, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = ReviewValidateSerializer
        serializer.is_valid(raise_exception=True)
        review_detail_api_view.text = request.data.get('text')
        review_detail_api_view.stars = request.data.get('stars')
        review_detail_api_view.product_id = request.data.get('pruduct_id')
        return Response(data={'review_id': review_detail_api_view.id}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        review_detail_api_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tag_api_view(request):
    if request.method == 'GET':
        tag_list = Tag.objects.all()
        data = ReviewSerializer(instance=tag_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = TagValidateSerializer
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        name = request.data.get('name')


        tag = Tag.objects.create(
            name=name
        )
        return Response(data={'tag_id': tag.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail_api_view(request):
    if request.method == 'GET':
        tag_list = Tag.objects.all()
        data = CategorySerializer(instance=tag_list, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = TagValidateSerializer
        serializer.is_valid(raise_exception=True)
        tag_detail_api_view.name = request.data.get('name')
        return Response(data={'tag_id': tag_detail_api_view.id}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        tag_detail_api_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
