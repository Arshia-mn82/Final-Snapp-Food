from django.urls import path
from food_app.views import Foodlist, UpdateFood

urlpatterns = [
    path('foodlist/', Foodlist.as_view()),
    path('delete_food/<int:pk>/', UpdateFood.as_view()),
]
