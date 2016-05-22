from django.shortcuts import render
from .models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return HttpResponse("Hello!")

@csrf_exempt
def store_user(request):
    
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    code = request.POST['code']
    user_profile = User()
    user_profile.username = username
    user_profile.password = password
    user_profile.email = email
    user_profile.code = code
    user_profile.save()
    return HttpResponse("1")

@csrf_exempt
def user_exists(request):
    
    username = request.POST['username']
    queryset = User.objects.all().filter(username=username)
    if(queryset.count() > 0):
        return HttpResponse("1")
    return HttpResponse("0")

@csrf_exempt
def  get_code(request):
    
    username = request.POST['username']
    queryset = User.objects.get(username=username)
    return HttpResponse(queryset.code)

@csrf_exempt
def  get_password(request):
    
    username = request.POST['username']
    queryset = User.objects.get(username=username)
    return HttpResponse(queryset.password)

@csrf_exempt
def make_verify(request):
    username = request.POST['username']
    queryset = User.objects.get(username=username)
    queryset.verified = "1"
    queryset.save()
    return HttpResponse("1")

@csrf_exempt
def is_verified(request):
    username = request.POST['username']
    queryset = User.objects.get(username=username)
    return HttpResponse(queryset.verified)


