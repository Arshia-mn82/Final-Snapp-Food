from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order_app.models import Order, OrderItem, Comment
from food_app.models import Food
from django.contrib.auth.models import User
from .serializer import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
import requests
import json
import environ

env = environ.Env()
environ.Env.read_env("./snappfood/.env")


class CreateOrderView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        input_food = data.get("input_food")
        input_num = data.get("input_num")
        user = User.objects.first()
        current_user = get_object_or_404(User, username=user)
        selected_food = Food.objects.get(name=input_food)
        if Order.objects.filter(user=current_user, paid=False).exists():
            current_order = Order.objects.get(user=current_user, paid=False)
            OrderItem.objects.create(
                order=current_order,
                food=selected_food,
                num=input_num,
            )
            json_result = find_delivery_cost(
                current_user.profile.x,
                current_user.profile.y,
                selected_food.restaurant.x,
                selected_food.restaurant.y,
            )

            current_order.delivery_cost = json_result.get("delivery_price")
            current_order.save()
        else:
            new_order = Order.objects.create(user=current_user)
            OrderItem.objects.create(
                order=new_order,
                food=selected_food,
                num=input_num,
            )
            json_result = (
                find_delivery_cost(
                    current_user.profile.x,
                    current_user.profile.y,
                    selected_food.restaurant.x,
                    selected_food.restaurant.y,
                ),
            )
            new_order.delivery_cost = json_result["delivery_price"]
            new_order.save()

        return JsonResponse(json_result, safe=False)


class AddCommentView(APIView):
    def post(self, request):
        data = request.data
        order_id = data.get("order_id")
        order = get_object_or_404(Order, order_id=order_id)
        comment_text = request.data.get("comment")
        if not comment_text:
            return Response(
                {"error": "Comment text is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        Comment.objects.create(user=request.user, order=order, comment=comment_text)
        return Response(
            {"message": "Comment added successfully"}, status=status.HTTP_201_CREATED
        )


class UpdateOrderStatusView(APIView):
    def patch(self, request, order_id):
        data = request.data
        order_id = data.get("order_id")
        order = get_object_or_404(Order, order_id=order_id)
        status_value = request.data.get("status")
        if status_value not in ["Pending", "Preparing", "Delivered", "Cancelled"]:
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )
        order.status = status_value
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)


class MarkOrderAsPaidView(APIView):
    def patch(self, request, order_id):
        data = request.data
        order_id = data.get("order_id")
        order = get_object_or_404(Order, order_id=order_id)
        if order.paid:
            return Response(
                {"error": "Order already marked as paid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        order.paid = True
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)


def find_delivery_cost(origin_lat, origin_long, destination_lat, destiantion_long):
    url = "http://45.139.10.8:8002/create_delivery/"
    api_key = env("LOGISITIC_API")
    data = {
        "origin_lat": origin_lat,
        "origin_long": origin_long,
        "destination_lat": destination_lat,
        "destiantion_long": destiantion_long
    }
    data = json.dumps(data)
    response = requests.post(
        url,
        headers={"API-KEY": f"{api_key}"},
        data=data,
    )
    print(response.content)
    print(type(response.content))
    json_file = json.loads(response.content)
    return JsonResponse(json_file , safe=False)
