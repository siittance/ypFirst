from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, filters
from .permission import *
from shop.models import *
from rest_framework import mixins

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_login', 'email', 'phone_number']


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_magazine', 'address_magazine']


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'product_description']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number']


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['catalog__product_name', 'order__order_number']


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['catalog__product_name', 'user__user_login']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__user_login', 'catalog__product_name', 'review_text']


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
