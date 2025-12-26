from django.urls import path
from .views import create_user, get_users

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('', get_users, name='get_users'),
]

