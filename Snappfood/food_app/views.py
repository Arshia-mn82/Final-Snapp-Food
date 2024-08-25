from django.views import View
from .models import Category,Food
from restaurant_app.models import Restaurant
from django.http import JsonResponse
from django.core import serializers


class Home(View):
    def get(self, request):
        try:
            restoran = Restaurant.objects.order_by('-created')[:5]
            categories = Category.objects.all()
            foods = Food.objects.filter(discount_spachial=True)

            categories_serialized = serializers.serialize('json', categories)
            food_offer_serialized = serializers.serialize('json', foods)
            restoran_serialized = serializers.serialize('json', restoran)

            return JsonResponse({
                'category': categories_serialized,
                'offer': food_offer_serialized,
                'restoran': restoran_serialized
            }, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)







