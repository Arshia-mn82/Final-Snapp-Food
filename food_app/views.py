from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Food
from .serializer import FoodSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied

class Foodlist(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super(Foodlist, self).get_permissions()

class UpdateFood(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["name"]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        food = super().get_object()
        if self.request.user != food.restaurant.owner:
            raise PermissionDenied("You do not have permission to update this food.")
        return food
