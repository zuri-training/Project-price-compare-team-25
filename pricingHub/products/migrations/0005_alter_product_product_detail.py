# Generated by Django 4.1 on 2022-08-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_comment_name_comment_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_detail',
            field=models.TextField(default='detail', max_length=200),
        ),
    ]
