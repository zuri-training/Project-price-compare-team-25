from django.shortcuts import render
from .models import Review
# Create your views here.


def review(request):
    reviews = Review.objects.all()
    return render(request, '', {'reviews': reviews})
