# Generated by Django 4.1.2 on 2022-12-14 10:07

import store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=store.models.product_photo),
        ),
    ]
