from django.core import serializers
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile, Product, Review, Cart, Order


def index(request):
    return HttpResponse("Hello!")

@csrf_exempt
def get_user(request):
    username = request.POST['username']
    queryset=UserProfile.objects.all().filter(username=username)
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def get_user_by_code(request):
    code = request.POST['code']
    queryset=UserProfile.objects.all().filter(code=code)
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def set_user(request):
    user_profile = UserProfile()
    user_profile.username = request.POST['username']
    user_profile.password = request.POST['password']
    user_profile.email = request.POST['email']
    user_profile.picture = request.POST['picture']
    user_profile.code = request.POST['code']
    user_profile.verified = request.POST['verified']
    user_profile.save()
    return HttpResponse("1")


@csrf_exempt
def get_product(request):
    productid = request.POST['productid']
    queryset = Product.objects.all().filter(id = productid)
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def set_product(request):
    product = Product.objects.get(id=request.POST['productid'])
    product.count = int(request.POST['count'])
    product.sold = int(request.POST['sold'])
    product.save()
    return HttpResponse("1")

@csrf_exempt
def get_products(request):
    queryset = Product.objects.all().order_by('-sold')
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def get_products_by_category(request):
    category = request.POST['category']
    queryset = Product.objects.all().filter(category=category).order_by('-sold')
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def get_products_by_query(request):
    query = request.POST['query']
    queryset1 = Product.objects.all().filter(name__icontains=query).order_by('-sold')
    queryset2 = Product.objects.all().filter(details__icontains=query).order_by('-sold')
    
    queryset = list()
    for product in queryset1:
        if product not in queryset:
            queryset.append(product)
    for product in queryset2:
        if product not in queryset:
            queryset.append(product)

    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def get_reviews(request):
    productid = request.POST['productid']
    queryset = Review.objects.all().filter(productid = productid)
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def set_review(request):
    review = Review.objects.all().filter(username = request.POST['username'], productid = request.POST['productid'])
    if review.count() > 0:
        review.get(username = request.POST['username']).delete()
    review = Review()
    review.username = UserProfile.objects.get(username = request.POST['username'])
    review.productid = Product.objects.get(id = request.POST['productid'])
    review.rating = request.POST['rating']
    review.details = request.POST['details']
    review.save()
    
    return HttpResponse("1")

@csrf_exempt
def set_cart(request):
    cart = Cart.objects.all().filter(username = request.POST['username'], productid = request.POST['productid'])
    if cart.count() > 0:
        cart = cart.get(username = request.POST['username'])
        cart.count += int(request.POST['count'])
    else:
        cart = Cart()
        cart.username = UserProfile.objects.get(username = request.POST['username'])
        cart.productid = Product.objects.get(id = request.POST['productid'])
        cart.count = int(request.POST['count'])
    cart.save()
    
    return HttpResponse("1")

@csrf_exempt
def get_carts(request):
    queryset = Cart.objects.all().filter(username = request.POST['username'])
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")

@csrf_exempt
def del_carts(request):
    carts = Cart.objects.all().filter(username=request.POST['username'])
    for cart in carts:
        cart.delete()
    return HttpResponse("1")

@csrf_exempt
def del_cart(request):
    carts = Cart.objects.all().filter(username=request.POST['username'], productid=request.POST['productid'])
    cart = carts.get(productid=request.POST['productid']).delete()
    return HttpResponse("1")

@csrf_exempt
def set_order(request):
    order = Order()
    order.username = UserProfile.objects.get(username = request.POST['username'])
    order.productid = Product.objects.get(id = request.POST['productid'])
    order.count = request.POST['count']
    order.delivstatus = request.POST['delivstatus']
    order.orderid = request.POST['orderid']
    order.duedate = request.POST['duedate']
    order.contactno = request.POST['contactno']
    order.address = request.POST['address']
    order.amount = request.POST['amount']
    order.paymentmethod = request.POST['paymentmethod']
    order.paymentinfo = request.POST['paymentinfo']
    order.save()
    return HttpResponse("1")

@csrf_exempt
def get_orders(request):
    queryset = Order.objects.all().filter(username=request.POST['username'], delivstatus=request.POST['delivstatus'])
    queryset=serializers.serialize('xml',queryset)
    return HttpResponse(queryset,content_type="application/xml")






