from . models import Comment, Product, Category
from django.shortcuts import render
from . forms import CreateComments
from django.views.generic import CreateView
from django.urls import reverse_lazy


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
    comments = Comment.objects.all
    return render(request, 'createcomment.html', {'comments': comments})


class AddCommentView(CreateView):
    model = Comment
    form_class = CreateComments
    template_name = 'product_detail.html'
    #fields = '__all__'

    success_url = reverse_lazy('comment')