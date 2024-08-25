from django.urls import path,include
from . import views

urlpatterns = [
    path('<str:categoryname>', views.CategoryShow.as_view()),
    path('restoran/<int:idr>', views.FoodShow.as_view()),

]
