from django.views import View
from .models import Category,Food
from restaurant_app.models import Restaurant
from django.http import JsonResponse
from .serializer import FoodSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView

class Foodlist(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer








