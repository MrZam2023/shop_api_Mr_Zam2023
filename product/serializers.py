from rest_framework import serializers
from product.models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars product_id'.split()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'id name'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100, min_length=3)
    description = serializers.CharField(required=False)
    price = serializers.FloatField()
    category_id = serializers.IntegerField(min_value=1)

    def validate_product_exists(product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist")

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)

    def validate_category_exists(category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("Category does not exist")

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    stars = serializers.FloatField(min_value=1, max_value=5)
    product_id = serializers.IntegerField(min_value=1)

    def validate_review_exists(review_id):
        try:
            Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise ValidationError("Review does not exist")


class TagValidateSerializer(serializers.Serializer):
    def validate_tag_exists(tag_ids):
        for tag_id in tag_ids:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                raise ValidationError("Tag does not exist")