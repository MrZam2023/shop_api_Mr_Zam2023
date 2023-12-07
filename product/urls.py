from django.urls import path

from . import admin, views
from .views import *
from users import views as users_views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view()),
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:id>/', views.ProductDetailAPIView.as_view()),
    path('reviews/', views.ReviewListAPIView.as_view()),
    path('reviews/<int:id>/',views.ReviewDetailAPIView.as_view()),
]