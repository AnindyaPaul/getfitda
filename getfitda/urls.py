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
    url(r'^$',views. index,name='index'),
    
    url(r'^get_user/', views.get_user, name='get_user'),
    url(r'^get_user_by_code/', views.get_user_by_code, name='get_user_by_code'),
    url(r'^set_user/',views.set_user,name='set_user'),
    
    url(r'^get_product/', views.get_product, name='get_product'),
    url(r'^set_product/', views.set_product, name='set_product'),
    url(r'^get_products/', views.get_products, name='get_products'),
    url(r'^get_products_by_category/', views.get_products_by_category, name='get_products_by_category'),
    url(r'^get_products_by_query/', views.get_products_by_query, name='get_products_by_query'),
    
    url(r'^get_reviews/', views.get_reviews, name='get_reviews'),
    url(r'^set_review/', views.set_review, name='set_review'),
    
    url(r'^get_carts/', views.get_carts, name='get_carts'),
    url(r'^set_cart/', views.set_cart, name='set_cart'),
    url(r'^del_cart/', views.del_cart, name='del_cart'),
    url(r'^del_carts/', views.del_carts, name='del_carts'),
    
    url(r'^get_orders/', views.get_orders, name='get_orders'),
    url(r'^set_order/', views.set_order, name='set_order'),
]
