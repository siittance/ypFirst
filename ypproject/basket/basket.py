from decimal import Decimal
from shop.models import Catalog

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket_session')
        if not basket:
            basket = self.session['basket_session'] = {}
        self.basket = basket

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Catalog.objects.filter(id__in=product_ids)

        basket = self.basket.copy()
        for product in products:
            basket[str(product.pk)]['catalog'] = product

        for item in basket.values():
            item['product_price'] = Decimal(item['product_price'])
            item['total_price'] = item['product_price'] * item['count']
            yield item

    # Добавил update_count с дефолтом False
    def add(self, catalog_obj, count=1, update_count=False):
        product_id = str(catalog_obj.id)
        if product_id in self.basket:
            if update_count:
                self.basket[product_id]['count'] = count
            else:
                self.basket[product_id]['count'] += count
        else:
            self.basket[product_id] = {
                'count': count,
                'product_price': str(catalog_obj.product_price),
            }
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, catalog_obj):
        product_id = str(catalog_obj.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        self.session['basket_session'] = {}
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['product_price']) * item['count'] for item in self.basket.values())
