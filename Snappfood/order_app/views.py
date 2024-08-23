from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from order_app.models import Order, OrderItem
from food_app.models import Food
from django.contrib.auth.models import User


def create_order(request, user, input_food, input_num):
    current_user = User.objects.get(username=user)
    new_order = Order.objects.create(user=current_user)
    selected_food = Food.objects.get(name=input_food)
    new_order_item = OrderItem.objects.create(order=new_order, foods=selected_food, num=input_num,
                                              price=selected_food.price)
    return HttpResponse("Order created successfully")


def new_create_order(request):
    if request.method == 'POST':
        return HttpResponse("OK")
    else:
        return HttpResponse("Bad request")
