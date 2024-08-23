from django.urls import path
from order_app.views import create_order, new_create_order
urlpatterns = [
    path('<str:user>/<str:input_food>/<int:input_num>', create_order),
    path('' , new_create_order)
]