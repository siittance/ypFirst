from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User, ProductCategory, Magazine, Catalog, Order, PosOrder, Cart, Review, Promotion
from .forms import ProductCategoryForm, MagazineForm, CatalogForm, PosOrderForm, CartForm, \
    ReviewForm, PromotionForm, RegistrationForm, LoginForm
from basket.forms import OrderForm


def first_view(request):
    products = Catalog.objects.all()
    categories = ProductCategory.objects.all()
    promotions = Promotion.objects.all()
    return render(request, 'first.html', {'products': products, 'categories': categories, 'promotions': promotions})

def second_view(request):
    categories = ProductCategory.objects.all()
    return render(request, 'second_html.html', {'categories': categories})

def third_view(request):
    categories = ProductCategory.objects.all()
    return render(request, 'third.html', {'categories': categories})

def map_view(request):
    categories = ProductCategory.objects.all()
    return render(request, 'map.html', {'categories': categories})

def product_view(request):
    products = Catalog.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'product.html', {'products': products, 'categories': categories})

def basket_view(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.price * item.quantity for item in cart_items)
    categories = ProductCategory.objects.all()
    return render(request, 'basket.html', {'cart_items': cart_items, 'total_price': total_price, 'categories': categories})

class CategoryDetailView(DetailView):
    model = ProductCategory
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Catalog.objects.filter(product_category=self.object)
        context['category_name'] = self.object.category_name
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Catalog
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'product_category/product_category_list.html'
    context_object_name = 'categories'

class ProductCategoryDetailView(DetailView):
    model = ProductCategory
    template_name = 'product_category/product_category_detail.html'
    context_object_name = 'category'

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product_category/product_category_form.html'
    success_url = reverse_lazy('product_category_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Категория успешно создана!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании категории.')
        return super().form_invalid(form)

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product_category/product_category_form.html'
    success_url = reverse_lazy('product_category_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Категория успешно обновлена!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении категории.')
        return super().form_invalid(form)

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'product_category/product_category_confirm_delete.html'
    success_url = reverse_lazy('product_category_list')
    context_object_name = 'category'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Категория успешно удалена!')
        return response

class MagazineListView(ListView):
    model = Magazine
    template_name = 'magazine/magazine_list.html'
    context_object_name = 'magazines'

class MagazineDetailView(DetailView):
    model = Magazine
    template_name = 'magazine/magazine_detail.html'
    context_object_name = 'magazine'

class MagazineCreateView(CreateView):
    model = Magazine
    form_class = MagazineForm
    template_name = 'magazine/magazine_form.html'
    success_url = reverse_lazy('magazine_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Магазин успешно создан!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании магазина.')
        return super().form_invalid(form)

class MagazineUpdateView(UpdateView):
    model = Magazine
    form_class = MagazineForm
    template_name = 'magazine/magazine_form.html'
    success_url = reverse_lazy('magazine_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Магазин успешно обновлен!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении магазина.')
        return super().form_invalid(form)

class MagazineDeleteView(DeleteView):
    model = Magazine
    template_name = 'magazine/magazine_confirm_delete.html'
    success_url = reverse_lazy('magazine_list')
    context_object_name = 'magazine'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Магазин успешно удален!')
        return response

class CatalogListView(ListView):
    model = Catalog
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'catalogs'

class CatalogDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/catalog_detail.html'
    context_object_name = 'catalog'

class CatalogCreateView(CreateView):
    model = Catalog
    form_class = CatalogForm
    template_name = 'catalog/catalog_form.html'
    success_url = reverse_lazy('catalog_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Товар успешно создан!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании товара.')
        return super().form_invalid(form)

class CatalogUpdateView(UpdateView):
    model = Catalog
    form_class = CatalogForm
    template_name = 'catalog/catalog_form.html'
    success_url = reverse_lazy('catalog_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Товар успешно обновлен!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении товара.')
        return super().form_invalid(form)

class CatalogDeleteView(DeleteView):
    model = Catalog
    template_name = 'catalog/catalog_confirm_delete.html'
    success_url = reverse_lazy('catalog_list')
    context_object_name = 'catalog'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Товар успешно удален!')
        return response

class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Заказ успешно создан!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании заказа.')
        return super().form_invalid(form)

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Заказ успешно обновлен!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении заказа.')
        return super().form_invalid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
    context_object_name = 'order'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Заказ успешно удален!')
        return response

class PosOrderListView(ListView):
    model = PosOrder
    template_name = 'pos_order/pos_order_list.html'
    context_object_name = 'pos_orders'

class PosOrderDetailView(DetailView):
    model = PosOrder
    template_name = 'pos_order/pos_order_detail.html'
    context_object_name = 'pos_order'

class PosOrderCreateView(CreateView):
    model = PosOrder
    form_class = PosOrderForm
    template_name = 'pos_order/pos_order_form.html'
    success_url = reverse_lazy('pos_order_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Позиция заказа успешно создана!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании позиции заказа.')
        return super().form_invalid(form)

class PosOrderUpdateView(UpdateView):
    model = PosOrder
    form_class = PosOrderForm
    template_name = 'pos_order/pos_order_form.html'
    success_url = reverse_lazy('pos_order_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Позиция заказа успешно обновлена!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении позиции заказа.')
        return super().form_invalid(form)

class PosOrderDeleteView(DeleteView):
    model = PosOrder
    template_name = 'pos_order/pos_order_confirm_delete.html'
    success_url = reverse_lazy('pos_order_list')
    context_object_name = 'pos_order'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Позиция заказа успешно удалена!')
        return response

class CartListView(ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'carts'

class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

class CartCreateView(CreateView):
    model = Cart
    form_class = CartForm
    template_name = 'cart/cart_form.html'
    success_url = reverse_lazy('cart_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Корзина успешно создана!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании корзины.')
        return super().form_invalid(form)

class CartUpdateView(UpdateView):
    model = Cart
    form_class = CartForm
    template_name = 'cart/cart_form.html'
    success_url = reverse_lazy('cart_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Корзина успешно обновлена!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении корзины.')
        return super().form_invalid(form)

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart/cart_confirm_delete.html'
    success_url = reverse_lazy('cart_list')
    context_object_name = 'cart'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Корзина успешно удалена!')
        return response

class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Отзыв успешно создан!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании отзыва.')
        return super().form_invalid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Отзыв успешно обновлен!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении отзыва.')
        return super().form_invalid(form)

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')
    context_object_name = 'review'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Отзыв успешно удален!')
        return response

class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion/promotion_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotion/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Акция успешно создана!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при создании акции.')
        return super().form_invalid(form)

class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Акция успешно обновлена!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении акции.')
        return super().form_invalid(form)

class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'promotion/promotion_confirm_delete.html'
    success_url = reverse_lazy('promotion_list')
    context_object_name = 'promotion'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Акция успешно удалена!')
        return response

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('product_view')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', context={'form': form})


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('product_view')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('product_view')