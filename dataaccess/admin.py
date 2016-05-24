from django.contrib import admin

# Register your models here.
from .models import UserProfile, Category, Product, Review, Cart, Order

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Order)