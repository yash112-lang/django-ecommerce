# Generated by Django 3.1.7 on 2021-07-18 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20210718_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 16, 57, 24, 372681)),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='product_images',
            field=models.ImageField(upload_to=''),
        ),
    ]