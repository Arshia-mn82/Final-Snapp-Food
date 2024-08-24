from django.shortcuts import render
from .models import Restaurant
from django.views import View
from django.core import serializers
from django.http import JsonResponse


class CategoryShow(View):
    def get(self,request,categoryname):
        food = Restaurant.objects.filter(category__name=categoryname)
        if food.exists:
            categories_serialized = serializers.serialize('json', food)
            return JsonResponse(categories_serialized, safe=False)