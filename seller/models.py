from django.core.files.base import ContentFile
from django.db import models
import datetime
import random
import array
from django.conf import settings

# Create your models here.

def generate():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
            '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    
    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    MAX_LEN = 10
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    item_id = ""
    for x in temp_pass_list:
            item_id = item_id + x
    return item_id

class add_product(models.Model):
    username = models.CharField(max_length=255, default=None)
    product_name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    price = models.IntegerField(default=None)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    product_description = models.TextField()
    current_Price = models.IntegerField(default=None)
    item_id = models.CharField(max_length=255, default=generate())
    product_images = models.FileField(blank=True)
