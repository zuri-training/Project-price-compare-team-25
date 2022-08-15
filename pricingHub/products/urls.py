from django.urls import path
from . import views
from .views import AddCommentView


urlpatterns = [
    path('category/', views.category, name='category'),
    path('product/', views.Product, name='product'),
    path('product_details/comment/', views.comment, name='comment'),
    path('comment/add_comment', AddCommentView.as_view(), name='add_comment'),
    path('<int:id>', views.product_details, name='product_details'),
]
