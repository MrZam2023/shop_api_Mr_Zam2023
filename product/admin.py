from django.contrib import admin
from .models import Product, Review, Category,Tag


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.
