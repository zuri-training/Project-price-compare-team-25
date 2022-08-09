from django.forms import ModelForm
from . models import Comment
from . models import  Product

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'