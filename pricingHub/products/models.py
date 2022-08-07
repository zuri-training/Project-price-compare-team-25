from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products:filtered_products', args=[self.slug])



    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    url_jumia = models.CharField(max_length=250, db_index=True)
    url_konga = models.CharField(max_length=250, db_index=True)
    url_kara = models.CharField(max_length=250, db_index=True)

    #price_kara = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price_kara = models.TextField(max_length=15, null=True, blank=True)
    price_jumia = models.TextField(max_length=15, null=True, blank=True)
    price_konga = models.TextField(max_length=15, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True)
    # make all thumbnails at most 140x140pixels

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

