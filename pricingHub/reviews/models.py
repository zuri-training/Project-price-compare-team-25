from django.db import models
from django.contrib.auth import get_user_model


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="Reviews")
    rating = models.IntegerField(default=0)
    review_text = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text
