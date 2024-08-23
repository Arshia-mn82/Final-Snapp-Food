from django.contrib import admin

from restaurant_app.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

