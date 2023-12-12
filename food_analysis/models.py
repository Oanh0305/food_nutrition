from django.db import models


class FoodItem(models.Model):
    fdcId = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1000)


class FoodNutrient(models.Model):
    number = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200)


class FoodNutrientInItem(models.Model):
    key = models.CharField(primary_key=True, max_length=20)
    food_item = models.ForeignKey(to=FoodItem, on_delete=models.CASCADE)
    food_nutrient = models.ForeignKey(to=FoodNutrient, on_delete=models.CASCADE)
    amount = models.FloatField()
    unit_name = models.CharField(max_length=10)
