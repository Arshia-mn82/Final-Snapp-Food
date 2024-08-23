from django.contrib import admin
from food_app.models import Food,Category,Rate

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass



    
