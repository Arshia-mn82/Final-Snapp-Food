from django.http.response import HttpResponse,JsonResponse


def welcome(request):
    return HttpResponse("Welcome to RESTAURANT")
