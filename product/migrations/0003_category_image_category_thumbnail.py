# Generated by Django 4.2 on 2023-10-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image'),
        ),
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail_image'),
        ),
    ]