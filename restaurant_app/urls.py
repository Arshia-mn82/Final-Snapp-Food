from django.urls import path
from restaurant_app.views import RestaurantList

urlpatterns = [
    path('restaurantlist/', RestaurantList.as_view()),
]
