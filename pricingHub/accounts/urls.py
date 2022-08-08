from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
     path('password_reset/', 
     auth_views.PasswordResetView.as_view(template_name = "registration/password_reset_form.html"), 
     name='password_reset'),
    path('password_reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
      name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
     name='password_reset_confirm'),
    path('reset/done/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
    name='password_reset_complete'),
]