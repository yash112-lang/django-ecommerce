# Generated by Django 3.1.7 on 2021-07-19 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0013_add_product_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_product',
            name='username',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
