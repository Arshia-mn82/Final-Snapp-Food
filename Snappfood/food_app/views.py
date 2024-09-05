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
    DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAdminUser , IsAuthenticated


class Foodlist(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        elif self.request.method == "POST":
            self.permission_classes = [IsAdminUser]

        return super(Foodlist, self).get_permissions()


class Food(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    
class DeleteFood(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        return self.queryset.filter(owner=self.request.user).delete()

class AddFood(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)