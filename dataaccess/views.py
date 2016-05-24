from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile, Product, Review


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


