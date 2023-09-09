from django.shortcuts import render, redirect
from .models import Products
from django.db import models
from django.core.paginator import Paginator
import random


# Create your views here.

# def home(request):
#     products = Products.objects.all()
#     return render(request, 'inventory/home.html', {'products': products})

def index(request):
    return render(request, "inventory/index.html")

def generate_products(request):
    if request.method == 'POST':

        for i in range(1, 51):
            product_name = f"Item {i}"
            stock_on_hand = random.randint(0, 50)
            product = Products.objects.create(product_name=product_name, stock_on_hand=stock_on_hand)
            product.save()

    # Paginate the products
    products = Products.objects.all()
    paginator = Paginator(products, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "inventory/generate_products.html", {"page_obj": page_obj})



def sort_asc(request):
    products = Products.objects.all().order_by("product_name")
    # products = Products.objects.order_by('product_name')
    return render(request, 'inventory/sort_asc.html', {'products': products})


def sort_desc(request):
    products = Products.objects.all().order_by('-stock_on_hand')
    return render(request, 'inventory/sort_desc.html', {'products': products})


def reduce_stock(request):
    products = Products.objects.all()
    for product in products:
        if product.stock_on_hand > 1:
            product.stock_on_hand -= 2
        else:
            product.Stock_On_Hand = 0
        product.save()
    return render(request, 'inventory/reduce_stock.html', {'products': Products.objects.all()})


def update_even_stock(request):
    # Filter out values containing even numbers and iterate over them
    products = Products.objects.all()
    for product in products:
        if product.id % 2 == 0:
            product.stock_on_hand += 2
        product.save()

    return render(request, 'inventory/update_even_stock.html', {'products': Products.objects.all()})
