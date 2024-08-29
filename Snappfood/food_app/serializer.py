from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Food
        fields = '__all__'
