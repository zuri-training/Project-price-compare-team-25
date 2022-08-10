from django.urls import path
from . import views
app_name = "reviews"

urlpatterns = [
    path('reviews', views.reviews, name='reviews')
]