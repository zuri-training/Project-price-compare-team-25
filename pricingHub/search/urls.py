from django.urls import path, include
from . import views

urlpatterns = [
    path('search-venues', views.search_venues, name='search-venues'),
]