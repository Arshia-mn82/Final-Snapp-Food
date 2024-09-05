from django.views import View
from .models import Category, Food
from restaurant_app.models import Restaurant
from django.http import JsonResponse
from .serializer import FoodSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)


class Foodlist(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class Food(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
