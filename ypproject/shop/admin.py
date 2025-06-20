from django.contrib import admin
from .models import (
    User, ProductCategory, Magazine, Catalog,
    Order, PosOrder, Cart, Review, Promotion
)





@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('name_magazine', 'address_magazine')
    search_fields = ('name_magazine', 'address_magazine')


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'quantity', 'product_category', 'magazine')
    list_filter = ('product_category', 'magazine')
    search_fields = ('product_name',)
    readonly_fields = ('image',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('sum_bill', 'date_order', 'user')
    list_filter = ('date_order',)
    search_fields = ('order_number', 'user__user_login')


@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    list_display = ('catalog', 'order', 'count')
    list_filter = ('order',)
    search_fields = ('catalog__product_name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'catalog', 'quantity', 'price')
    search_fields = ('user__user_login', 'catalog__product_name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'catalog', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__user_login', 'catalog__product_name')


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title',)
    readonly_fields = ('image',)
