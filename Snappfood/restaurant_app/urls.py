from django.urls import path,include
from . import views

urlpatterns = [
    path('<str:categoryname>', views.CategoryShow.as_view()),

]
