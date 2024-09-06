from . import views
from django.urls import path

urlpatterns = [
    path('foodlist/' , views.Foodlist.as_view()),
    path('food/' , views.Food.as_view()),
]