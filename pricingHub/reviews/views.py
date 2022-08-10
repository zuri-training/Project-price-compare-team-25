from django.shortcuts import render
from .models import reviews

# Create your views here.
def review(request):
    revieww = reviews.objects.all()
    return render(request, 'product.html', {'comments': reviews})
