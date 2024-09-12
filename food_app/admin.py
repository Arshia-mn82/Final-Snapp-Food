from django.contrib import admin
from food_app.models import Food,Category,Rate

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'restaurant', 'discount_special', 'discount_rate')

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass



    
