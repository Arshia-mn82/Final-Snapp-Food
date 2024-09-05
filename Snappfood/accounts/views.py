from django.http.response import HttpResponse,JsonResponse
from .serializer import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Wallet

def welcome(request):
    return HttpResponse("Welcome to RESTAURANT")


class Register(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    