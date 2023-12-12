from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import FoodItem, FoodNutrient, FoodNutrientInItem

admin.site.register(FoodItem)
admin.site.register(FoodNutrient)
admin.site.register(FoodNutrientInItem)