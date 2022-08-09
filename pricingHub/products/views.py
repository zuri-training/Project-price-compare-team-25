from . models import Comment, Product, Category
from django.shortcuts import render, redirect
from . form import CommentForm, ProductForm


def category(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def product(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def comment(request):
    comments = Comment.objects.all()
    return render(request, 'product.html', {'comments': comments})


def createcomment(request):
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('comment')

    else:
        return render(request, 'index.html', {'form': form})

def productdetail(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('comment')

    else:
        return render(request, 'productdetail.html', {'form': form})