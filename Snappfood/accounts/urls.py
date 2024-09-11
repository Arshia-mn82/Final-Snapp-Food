from django.urls import path
from .views import Register, Login, Refresh , welcome

urlpatterns = [
    path('welcome/', welcome),
    path('register/', Register.as_view()),
    path('login/', Login.as_view(), name='token_obtain_pair'),
    path('refresh/', Refresh.as_view(), name='token_refresh'),
]
