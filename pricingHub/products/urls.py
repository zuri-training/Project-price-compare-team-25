from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('comment/', views.comment, name='comment'),
    path('product_details', views.product_details, name='product_details'),
]
