from django.contrib import admin
from restaurant_app.models import Restaurant,Category


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
