
from django import template
from sale.models import SaleOrderLine,SaleOrder
from django.contrib.auth.models import User
from customer.models import Customer

register = template.Library()


@register.filter
def cart_item_count(user):
    if not user.is_authenticated:
        return 0
    try:
        customer_obj = Customer.objects.get(user=user)
    except:
        return 0

    if user.is_authenticated:
        qs = SaleOrder.objects.filter(customer=customer_obj, status='q')
        if qs.exists():
            return qs[0].so_lines.count()
    return 0
    