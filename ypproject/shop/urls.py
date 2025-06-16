from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view, name='home'),
    path('about/', views.second_view, name='second_view'),
    path('contacts/', views.third_view, name='third_view'),
    path('map/', views.map_view, name='map_view'),
    path('products/', views.product_view, name='product_view'),
    path('basket/', views.basket_view, name='basket_view'),

    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),

    path('product_categories/', views.ProductCategoryListView.as_view(), name='product_category_list'),
    path('product_categories/<int:pk>/', views.ProductCategoryDetailView.as_view(), name='product_category_detail'),
    path('product_categories/create/', views.ProductCategoryCreateView.as_view(), name='product_category_create'),
    path('product_categories/<int:pk>/update/', views.ProductCategoryUpdateView.as_view(),
         name='product_category_update'),
    path('product_categories/<int:pk>/delete/', views.ProductCategoryDeleteView.as_view(),
         name='product_category_delete'),

    path('magazines/', views.MagazineListView.as_view(), name='magazine_list'),
    path('magazines/<int:pk>/', views.MagazineDetailView.as_view(), name='magazine_detail'),
    path('magazines/create/', views.MagazineCreateView.as_view(), name='magazine_create'),
    path('magazines/<int:pk>/update/', views.MagazineUpdateView.as_view(), name='magazine_update'),
    path('magazines/<int:pk>/delete/', views.MagazineDeleteView.as_view(), name='magazine_delete'),

    path('catalogs/', views.CatalogListView.as_view(), name='catalog_list'),
    path('catalogs/<int:pk>/', views.CatalogDetailView.as_view(), name='catalog_detail'),
    path('catalogs/create/', views.CatalogCreateView.as_view(), name='catalog_create'),
    path('catalogs/<int:pk>/update/', views.CatalogUpdateView.as_view(), name='catalog_update'),
    path('catalogs/<int:pk>/delete/', views.CatalogDeleteView.as_view(), name='catalog_delete'),

    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    path('pos_orders/', views.PosOrderListView.as_view(), name='pos_order_list'),
    path('pos_orders/<int:pk>/', views.PosOrderDetailView.as_view(), name='pos_order_detail'),
    path('pos_orders/create/', views.PosOrderCreateView.as_view(), name='pos_order_create'),
    path('pos_orders/<int:pk>/update/', views.PosOrderUpdateView.as_view(), name='pos_order_update'),
    path('pos_orders/<int:pk>/delete/', views.PosOrderDeleteView.as_view(), name='pos_order_delete'),

    path('carts/', views.CartListView.as_view(), name='cart_list'),
    path('carts/<int:pk>/', views.CartDetailView.as_view(), name='cart_detail'),
    path('carts/create/', views.CartCreateView.as_view(), name='cart_create'),
    path('carts/<int:pk>/update/', views.CartUpdateView.as_view(), name='cart_update'),
    path('carts/<int:pk>/delete/', views.CartDeleteView.as_view(), name='cart_delete'),

    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),

    path('promotions/', views.PromotionListView.as_view(), name='promotion_list'),
    path('promotions/<int:pk>/', views.PromotionDetailView.as_view(), name='promotion_detail'),
    path('promotions/create/', views.PromotionCreateView.as_view(), name='promotion_create'),
    path('promotions/<int:pk>/update/', views.PromotionUpdateView.as_view(), name='promotion_update'),
    path('promotions/<int:pk>/delete/', views.PromotionDeleteView.as_view(), name='promotion_delete'),
]