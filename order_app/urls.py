from django.urls import path
from .views import CreateOrderView, AddCommentView, UpdateOrderStatusView, MarkOrderAsPaidView

urlpatterns = [
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('update_status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('mark_as_paid/', MarkOrderAsPaidView.as_view(), name='mark_order_as_paid'),
]
