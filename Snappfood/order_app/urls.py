from django.urls import path
from .views import CreateOrderView, AddCommentView, UpdateOrderStatusView, MarkOrderAsPaidView

urlpatterns = [
    path('create_order/<str:user>/<str:input_food>/<int:input_num>/', CreateOrderView.as_view(), name='create_order'),
    path('add_comment/<int:order_id>/', AddCommentView.as_view(), name='add_comment'),
    path('update_status/<int:order_id>/', UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('mark_as_paid/<int:order_id>/', MarkOrderAsPaidView.as_view(), name='mark_order_as_paid'),
]
