from typing import Counter
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Count
from seller.models import add_product as add_product_seller_to_database
import random
import array

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        data1 = add_product_seller_to_database.objects.filter(username=request.user)
        d = {}
        for data in data1:
            if(data.item_id not in d):
                d[data.item_id] = data
        context = {
            "data": d
        }
        return render(request, 'index.html', context)
    else:
        return redirect('credentials/login')

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

def add_product(request):
    if request.user.is_authenticated:
        return render(request, 'add_product.html')
    else:
        return redirect('/credentials/login')


def add_product_seller(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('description')
        category = request.POST.get('category')
        # images = request.FILES.get('myFile')
        # images = request.POST.getlist('myFile')
        product_price = request.POST.get('product_price')
        current_product_price = request.POST.get('current_product_price')
        item_id = generate()
        # print(images)
        for f in request.FILES.getlist('myFile'):
            a = add_product_seller_to_database(product_name=product_name, product_description=product_description, product_category=category, price=product_price, current_Price=current_product_price, product_images=f, username=request.user, item_id=item_id)
            a.save()
        return redirect('/seller/index')
    else:
        return redirect('credentials/login')

def update_item(request):
    if request.user.is_authenticated:
        item_id = request.GET.get('item_id')
        data = add_product_seller_to_database.objects.filter(item_id = item_id)
        context = {
            'data': data
        }
        return render(request, 'update_item.html', context)
    else:
        return redirect('credentials/login')

def update_item_seller(request):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            product_name = request.POST.get('product_name')
            product_description = request.POST.get('description')
            category = request.POST.get('category')
            images = request.FILES.get('myFile')
            product_price = request.POST.get('product_price')
            current_product_price = request.POST.get('current_product_price')
            item_id = request.GET.get('item_id')
            print("Till now executed successfully.")
            a = add_product_seller_to_database.objects.filter(item_id=item_id).update(product_name=product_name, product_description=product_description, product_category=category, price=product_price, current_Price=current_product_price, product_images=images)
            # a.save()
            return redirect('/seller/index')
        except Exception as e:
            return redirect('/seller/index')
    else:
        return redirect('credentials/login')
        
def delete_item(request):
    item_id = request.GET.get('item_id')
    add_product_seller_to_database.objects.filter(item_id=item_id).delete()
    return redirect('/seller/index')
    