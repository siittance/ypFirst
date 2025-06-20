from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='user')
router.register('product-categories', ProductCategoryViewSet, basename='productcategory')
router.register('magazines', MagazineViewSet, basename='magazine')
router.register('catalog', CatalogViewSet, basename='catalog')
router.register('orders', OrderViewSet, basename='order')
router.register('pos-orders', PosOrderViewSet, basename='posorder')
router.register('carts', CartViewSet, basename='cart')
router.register('reviews', ReviewViewSet, basename='review')
router.register('promotions', PromotionViewSet, basename='promotion')
urlpatterns += router.urls