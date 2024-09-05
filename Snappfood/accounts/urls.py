from accounts.views import welcome
from django.urls import path
from .views import Register
urlpatterns = [
    path('welcome/' , welcome),
    path('register/' , Register.as_view())
]