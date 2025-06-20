from django.urls import path
from .views import basket_remove, basket_detail, basket_clear, basket_buy, open_order, basket_add, orders_list

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('clear/', basket_clear, name='basket_clear'),
    path('buy/', basket_buy, name='basket_buy'),
    path('order_form/', open_order, name='order_open'),
    path('orders/', orders_list, name='orders_list'),
]