"""getfitda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dataaccess import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^store_user/',views.store_user,name='store_user'),
    url(r'^user_exists/',views.user_exists,name='user_exists'),
    url(r'^get_password/',views.get_password,name='get_password'),
    url(r'^get_code/',views.get_code,name='get_code'),
    url(r'^is_verified/',views.is_verified,name='is_verified'),
    url(r'^make_verify/',views.make_verify,name='make_verify'),
]
