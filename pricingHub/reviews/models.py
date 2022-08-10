from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
class reviews(models.Model):
    user=models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="reviews"
    )
    rating= models.IntegerField(max_length=5)
    review_text= models.TextField(max_length=200)
    date_created= models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        pass 

    def __str__(self):
        return self.review_text