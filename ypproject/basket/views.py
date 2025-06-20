from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from pyexpat.errors import messages
from shop.models import Catalog, Order, PosOrder

from . import forms
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
    count = int(request.POST.get('count', 1))

    basket.add(product, count=abs(count), update_count=(count < 0))

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
def orders_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_order')
    return render(request, 'order/orders_list.html', {'orders': orders})

@login_required
def open_order(request):
    basket = Basket(request)

    if not basket:
        messages.warning(request, "Ваша корзина пуста")
        return redirect('basket_detail')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.sum_bill = basket.get_total_price()
            order.save()

            for item in basket:
                PosOrder.objects.create(
                    catalog=item['catalog'],
                    count=item['count'],
                    order=order,
                )

            basket.clear()
            return redirect('orders_list')

        messages.error(request, "Исправьте ошибки в форме")
    else:
        initial = {
            'buyer_surname': request.user.last_name or '',
            'buyer_name': request.user.first_name or '',
        }
        form = OrderForm(initial=initial)

    return render(request, 'order/order_form.html', {
        'form': form,
        'basket': basket,
        'total_price': basket.get_total_price()
    })

