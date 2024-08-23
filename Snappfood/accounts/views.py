from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render

def welcome(request):
    return render(
        request,'accounts/welcome'
    )
