from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile


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