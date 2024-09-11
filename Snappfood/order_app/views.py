from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order_app.models import Order, OrderItem, Comment
from food_app.models import Food
from django.contrib.auth.models import User
from .serializer import OrderSerializer, OrderItemSerializer


class CreateOrderView(APIView):
    def post(self, request, user, input_food, input_num):
        current_user = get_object_or_404(User, username=user)
        selected_food = get_object_or_404(Food, name=input_food)
        new_order = Order.objects.create(user=current_user)
        OrderItem.objects.create(
            order=new_order,
            food=selected_food,
            num=input_num,
            price=selected_food.price,
            restaurant=selected_food.restaurant,
        )
        return Response(
            {"message": "Order created successfully"}, status=status.HTTP_201_CREATED
        )


class AddCommentView(APIView):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
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
        order = get_object_or_404(Order, id=order_id)
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
        order = get_object_or_404(Order, id=order_id)
        if order.paid:
            return Response(
                {"error": "Order already marked as paid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        order.paid = True
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
