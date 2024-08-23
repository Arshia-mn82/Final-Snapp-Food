from accounts.views import welcome
from django.urls import path
urlpatterns = [
    path('' , welcome)
]