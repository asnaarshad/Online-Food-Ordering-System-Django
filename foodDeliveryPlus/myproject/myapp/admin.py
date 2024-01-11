from django.contrib import admin
from .models import FoodCategory, FoodType, FoodItem, Order, About, Contact

admin.site.register(FoodCategory)
admin.site.register(FoodType)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(FoodItem)
admin.site.register(Order)