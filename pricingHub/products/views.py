from . models import Comment, Product, Category
from django.shortcuts import render


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def product(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def category(request):
    products = Product.objects.all()
    return render(request, 'category.html', {'products': products})

def product_details(request):
    return render(request, 'product_detail_page/product_detail.html')

def comment(request):
    comments = Comment.objects.all()
    return render(request, 'product.html', {'comments': comments})
