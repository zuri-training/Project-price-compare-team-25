# Generated by Django 4.1 on 2022-08-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_product_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_jumia',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_kara',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_konga',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
