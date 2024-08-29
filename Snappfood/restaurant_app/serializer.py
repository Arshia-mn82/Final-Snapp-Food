from rest_framework import serializers
from .models import Restaurant

class RestaurnatSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = Restaurant
        fields = '__all__'