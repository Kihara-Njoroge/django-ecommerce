from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'order.get_cart_items': 0, 'order.get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkOut(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'order.get_cart_items': 0, 'order.get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)
