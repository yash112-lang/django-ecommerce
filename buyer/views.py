from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from seller.models import add_product
from buyer.models import add_to_cart as buyer_add_to_cart

# Create your views here.

def index(request):
    data = add_product.objects.all()
    products = {}
    for product in data:
        if product.item_id not in products:
            products[product.item_id] = product
    product_images = {}

    discount = []

    for p in products.values():
        discount.append(int(((p.price - p.current_Price) / p.price) * 100))
    
    
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
    deal_of_the_day = deal_of_the_day_temp
    deal_of_the_day_discount = 100 * (deal_of_the_day[0].price - deal_of_the_day[0].current_Price) // deal_of_the_day[0].price
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

    cart_details = list(buyer_add_to_cart.objects.filter(user_id = request.user.email))

    cart_price = 0
    for i in cart_details:
        cart_price += products[i.product_id].current_Price
    
    cart_items_details = buyer_add_to_cart.objects.filter(user_id = request.user.email)
    c = []
    for i in cart_items_details:
        c.append(i.product_id)

    cart_items_details = c

    context = {
        'data': products,
        'product_images': product_images,
        'deal_of_the_day': deal_of_the_day,
        "deal_of_the_day_discount": deal_of_the_day_discount,
        "featured_cards": featured_cards,
        'discount': discount,
        "cart_items": [len(cart_details), cart_price],
        "cart_items_detail": cart_items_details
    }
    return render(request, 'newHome.html', context)

def add_to_cart(request):
    item_id = request.GET.get('item_id')
    cart_details = buyer_add_to_cart(user_id=request.user.email, product_id=item_id)
    cart_details.save()
    return redirect('/buyer/index')

def show_by_category(request):
    category_data = add_product.objects.filter(product_category=request.GET.get('category'))
    category_products = {}
    for product in category_data:
        if product.item_id not in category_products:
            category_products[product.item_id] = product
    products = {}
    data = add_product.objects.all()
    for product in data:
        if product.item_id not in products:
            products[product.item_id] = product
    
    cart_details = list(buyer_add_to_cart.objects.filter(user_id = request.user.email))

    cart_price = 0
    for i in cart_details:
        cart_price += products[i.product_id].current_Price
    context = {
        'data': category_products,
        "cart_items": [len(cart_details), cart_price],
        'category': request.GET.get('category')
    }
    return render(request, 'show_by_category.html', context)

def gotoCart(request):
    buyer_add_to_cart_details = buyer_add_to_cart.objects.filter(user_id=request.user.email)
    

    d = {}


    for i in buyer_add_to_cart_details:
        d[i.product_id] = [add_product.objects.filter(item_id=i.product_id)[0], i.date_added]
    context = {
        'd': d
    }
    return render(request, 'cart.html', context)

def removeItem(request):
    item_id = request.GET.get("item_id")
    buyer_add_to_cart.objects.filter(product_id=item_id).delete()
    return redirect("/buyer/gotoCart")

def gotoPaymentPage(request):
    if request.method == "POST":
        price = request.POST.get("price")
        context = {
            "price": price,
        }
        return render(request, "payment_page.html", context)

def search(request):
    search_object = request.GET.get("query")
    result = add_product.objects.filter(product_name__contains=search_object)

    data = add_product.objects.all()
    products = {}
    for product in data:
        if product.item_id not in products:
            products[product.item_id] = product
    cart_details = list(buyer_add_to_cart.objects.filter(user_id = request.user.email))
    cart_price = 0
    for i in cart_details:
        cart_price += products[i.product_id].current_Price
    
    d = {}

    discount = []

    for p in products.values():
        discount.append(int(((p.price - p.current_Price) / p.price) * 100))
    for i in result:
        if i not in d:
            d[i.item_id] = i
    context = {
        "search": d,
        "search_object": search_object,
        "discount": discount,
        "cart_items": [len(cart_details), cart_price],
        "number_search": len(list(d.keys())),
    }
    return render(request, "search_result.html", context)