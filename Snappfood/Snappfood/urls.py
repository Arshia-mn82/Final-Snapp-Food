from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/' , include('food_app.urls')),
    path('restaurant/', include('restaurant_app.urls')),
    path('welcome/' , include('accounts.urls')),

]
