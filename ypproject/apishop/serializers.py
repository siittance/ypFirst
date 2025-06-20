import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from rest_framework import serializers
from shop.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'user_login',
            'user_password',
            'email',
            'phone_number'
        ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'category_name'
        ]


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = [
            'id',
            'name_magazine',
            'address_magazine'
        ]


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            'id',
            'product_name',
            'product_description',
            'product_price',
            'image',
            'quantity',
            'product_category',
            'magazine'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'sum_bill',
            'date_order',
            'user'
        ]


class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosOrder
        fields = [
            'id',
            'catalog',
            'order',
            'count'
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'catalog',
            'quantity',
            'price'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'rating',
            'review_text',
            'created_at',
            'user',
            'catalog'
        ]


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = [
            'id',
            'title',
            'description',
            'image',
            'start_date',
            'end_date'
        ]
