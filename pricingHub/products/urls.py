from django.urls import path, re_path
from . import views

app_name = "products"

urlpatterns = [
    path('category/', views.category, name="category"),
    path('templates/products/', views.category, name="category"),
    path('product_detail/', views.product_detail, name="product_detail"),
    #path('templates/products/', views.product_detail, name="product_detail"),
]
