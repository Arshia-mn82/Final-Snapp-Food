from .models import Restaurant
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from food_app.models import Food
from .serializer import RestaurnatSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

# class CategoryShow(View):
#     def get(self, request, categoryname):
#         food = Restaurant.objects.filter(category__name=categoryname)
#         if food.exists():
#             categories_serialized = serializers.serialize('json', food)
#             return JsonResponse(categories_serialized, safe=False,status=200)
#         return JsonResponse({"message": "No food found in this category"}, status=404)

# class FoodShow(View):
#     def get(self, request, idr):
#         try:
#             restorans=Restaurant.objects.get(id=idr)
#             foods = Food.objects.filter(restaurant=restorans)
#             foods_serialized = serializers.serialize('json', foods)
#             return JsonResponse(foods_serialized, safe=False,status=200)
#         except Food.DoesNotExist:
#             return JsonResponse({"message": "Food not found"}, status=404)


class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurnatSerializer
    
