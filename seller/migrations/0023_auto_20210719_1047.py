# Generated by Django 3.1.7 on 2021-07-19 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0022_auto_20210719_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 10, 47, 5, 201580)),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='item_id',
            field=models.CharField(default='5zip3<X~r~', max_length=255),
        ),
    ]