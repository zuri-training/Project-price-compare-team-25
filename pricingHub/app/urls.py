from django.urls import path
from . import views

urlpatterns = [
   
    path('terms', views.terms, name= 'terms'),
    path('privacy', views.privacy, name= 'privacy'),
    path('contact', views.contact, name= 'contact'),
    path('faqs', views.faqs, name= 'faqs'),
]