from django.urls import path

from . import admin, views
from .views import *
from users import views as users_views

urlpatterns = [
    path('users/register/', users_views.register_api_view),
    path('users/login/', users_views.login_api_view),
]