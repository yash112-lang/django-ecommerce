from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Sum
from seller.models import add_product

# Create your views here.

def index(request):
    data = add_product.objects.all()
    products = {}
    for product in data:
        if product.item_id not in products:
            products[product.item_id] = product
    product_images = {}
    imageList = []
    # for image in data:
    #     if image.item_id not in product_images:
    #         product_images[image.item_id] = imageList
    #         product_images[image.item_id].append(image.product_images)
    #     else:
    #         product_images[image.item_id].append(image.product_images)
    # print(product_images)

    count = 0
    while(count < len(data)):
        if(data[count].item_id not in product_images):
            product_images[data[count].item_id] = [data[count].product_images]
        else:
            product_images[data[count].item_id].append(data[count].product_images)
        count += 1
    
    deal_of_the_day = add_product.objects.all()
    min = 999999
    deal_of_the_day_temp = []
    for product in deal_of_the_day:
        if(product.current_Price < min):
            min = product.current_Price
            deal_of_the_day_temp.clear()
            deal_of_the_day_temp.append(product)
    print(deal_of_the_day_temp)
    deal_of_the_day = deal_of_the_day_temp
    deal_of_the_day_discount = 100 * (deal_of_the_day[0].price - deal_of_the_day[0].current_Price) // deal_of_the_day[0].price
    print(deal_of_the_day_discount)
    featured_cards = add_product.objects.all()
    feature_card = {}
    count = 0
    for feature in featured_cards:
        if feature.item_id not in feature_card:
            feature_card[feature.item_id] = feature
            count += 1
            if(count == 3):
                break
    featured_cards = feature_card.values()
    context = {
        'data': products,
        'product_images': product_images,
        'deal_of_the_day': deal_of_the_day,
        "deal_of_the_day_discount": deal_of_the_day_discount,
        "featured_cards": featured_cards
    }
    return render(request, 'home.html', context)