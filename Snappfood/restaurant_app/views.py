from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Restaurant
from .serializer import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class RestaurantList(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

class UpdateRestaurant(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        restaurant = super().get_object()
        if self.request.user != restaurant.owner:
            raise PermissionDenied("You do not have permission to update this restaurant.")
        return restaurant
