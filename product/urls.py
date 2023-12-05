from django.urls import path

from . import admin, views
from .views import *
from users import views as users_views

urlpatterns = [
    path('categories/', views.category_api_view),
    path('products/', views.product_api_view),
    path('products/<int:id>/', views.product_detail_api_view),
    path('reviews/', views.review_api_view),
    path('reviews/<int:id>/',views.review_detail_api_view),
    path('users/register/', users_views.register_api_view),
    path('users/login/', users_views.login_api_view),
]