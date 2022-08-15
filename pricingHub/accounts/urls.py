from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home, name='homepage'),
    path('about', views.about, name = 'about'),
    path('register_user', views.register_user, name='register'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
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