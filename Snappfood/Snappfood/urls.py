from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/' , include('accounts.urls')),
    path('createorder/', include('order_app.urls')),
    path('newcreateorder/' , include('order_app.urls'))
]
