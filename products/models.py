from pickle import TRUE
from django.db import models
from django.urls import clear_script_prefix

# Create your models here.




class Category(models.Model):
    id = models.AutoField(primary_key= TRUE, null= False) 
    cat_name = models.CharField(max_length=225, db_index= True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





class Product(models.Model):
    id = models.AutoField(primary_key= TRUE, null= False)

    product_name = models.CharField(max_length=225, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    product_img = models.ImageField(default='', blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
     id = models.AutoField(primary_key= TRUE, null= False)
     comment_body = models.SlugField(max_length=225, unique=True, db_index=True)
     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
     created_on = models.DateTimeField(auto_now_add=True)
     modified_on = models.DateTimeField(auto_now=True)