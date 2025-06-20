from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop.models import Catalog, Order, PosOrder
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm

def basket_detail(request):
    basket = Basket(request)
    total_price = basket.get_total_price()
    return render(request, 'basket/detail.html', context={'basket': basket, 'total_price': total_price})

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Catalog, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Catalog, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']  # reload - булево поле, меняющее поведение добавления
        )
    return redirect('basket_detail')

@login_required
def basket_buy(request):
    basket = Basket(request)
    if len(basket) == 0:
        return redirect('basket_detail')

    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            buyer_surname=form.cleaned_data['buyer_surname'],
            buyer_name=form.cleaned_data['buyer_name'],
            buyer_middlename=form.cleaned_data.get('buyer_middlename', ''),
            comment=form.cleaned_data.get('comment', ''),
            delivery_address=form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type'],
            user=request.user,
            sum_bill=0
        )

        total_sum = 0
        for item in basket:
            PosOrder.objects.create(
                catalog=item['catalog'],
                count=item['count'],
                order=order
            )
            total_sum += item['product_price'] * item['count']

        order.sum_bill = total_sum
        order.save()

        basket.clear()
    return redirect('basket_detail')

@login_required
def open_order(request):
    context = {
        'form_order': OrderForm()
    }
    return render(request, 'order/order_form.html', context)
