from django.db import models
from datetime import datetime

# Create your models here.

class add_to_cart(models.Model):
    user_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    date_added = models.DateTimeField(default = datetime.now())