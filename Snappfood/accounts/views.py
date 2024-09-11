from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import APIKey
from .serializer import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def welcome(request):
    return HttpResponse("Welcome to the Snappfood app!")

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class Register(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        APIKey.objects.create(user=user)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        api_key = APIKey.objects.get(user=user)
        return Response({"message": "User created", "api_key": api_key.key})
