from django.urls import path
from .views import *

urlpatterns = [
    path('', first_view, name='home'),
    path('second/', second_view, name='second_view'),
    path('third/', third_view, name='third_view'),
    path('map/', map_view, name='map_view'),
    path('product/', product_view, name='product_view'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('basket/', basket_view, name='basket_view'),
]
