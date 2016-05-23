from django.contrib import admin

# Register your models here.
from .models import UserProfile, Category, Product

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)