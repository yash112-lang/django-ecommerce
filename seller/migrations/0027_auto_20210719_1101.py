# Generated by Django 3.1.7 on 2021-07-19 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0026_auto_20210719_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 11, 1, 5, 212069)),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='item_id',
            field=models.CharField(default='3~h7*iW#Si', max_length=255),
        ),
    ]