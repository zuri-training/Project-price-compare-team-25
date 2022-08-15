from .models import Comment, Product, Category
from django.shortcuts import render, get_object_or_404
from . forms import CreateComments
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateComments
from .models import Comment


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def product(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def category(request):
    products = Product.objects.all()
    return render(request, 'category.html', {'products': products})

  
def product_details(request, id):
    products = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html' , {'products': products})


def comment(request):
    comments = get_object_or_404(Comment, pk=id)
    return render(request, 'createcomment.html', {'comments': comments})



class AddCommentView(CreateView):
    model = Comment
    form_class = CreateComments
    template_name = 'product_detail.html'
    #fields = '__all__'

<<<<<<< HEAD
    success_url = reverse_lazy('comment')
=======
    success_url = reverse_lazy('comment')
def post_detailview(request, id):
   
  if request.method == 'POST':
    cf = CreateComments(request.POST or None)
    if cf.is_valid():
      content = request.POST.get('content')
      comment = Comment.objects.create(post = post, user = request.user, content = content)
      comment.save()
      return redirect(post.get_absolute_url())
    else:
      cf = CreateComments()
       
    context ={
      'comment_form':cf,
      }
    return render(request, 'comment.html', context)

>>>>>>> 1c5f1e4af9d5b24d68fdc7f32199de964be40ef7
