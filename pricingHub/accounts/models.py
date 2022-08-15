from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.
# class RegisterUserForm(UserCreationForm):
#     email = forms.EmailField()
#     full_name = forms.CharField(max_length=80)

#     class Meta:
#         model = User
#         fields = ('username', 'full_name', 'email')