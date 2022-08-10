from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# create your views here


def category(request):
    category = Category.objects.all()
    return render(request, "products/category.html", {"category": category})


def product_detail(request):
    product_detail = Product.objects.all()
    return render(request, "products/product_detail.html", {"product_detail": product_detail})
