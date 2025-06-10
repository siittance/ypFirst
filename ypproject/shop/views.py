from django.shortcuts import render

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second_html.html')

def third_view(request):
    return render(request, 'third.html')

def map_view(request):
    return render(request, 'map.html')

def product_view(request):
    return render(request, 'product.html')

def basket_view(request):
    return render(request, 'basket.html')

def category_detail(request, category_id):
    category_names = {
        1: 'Свадебный букет',
        2: 'Сладкий букет',
        3: 'Классика',
    }
    name = category_names.get(category_id, 'Неизвестная категория')
    return render(request, 'category_detail.html', {'category_name': name})
