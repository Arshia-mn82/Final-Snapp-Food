from django.views import View
from .models import Category,Food
from django.http import JsonResponse
from django.core import serializers

class Home(View):
    def get(self, request):
        categories = Category.objects.all()
        categories_serialized = serializers.serialize('json', categories)
        return JsonResponse(categories_serialized, safe=False)







