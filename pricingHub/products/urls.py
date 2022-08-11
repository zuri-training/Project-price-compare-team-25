from django.urls import path
from . import views


urlpatterns = [
    path('category', views.category, name='category'),
    path('product', views.product, name='product'),
    path('comment', views.comment, name='comment'),
]
