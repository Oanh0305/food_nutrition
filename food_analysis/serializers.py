from rest_framework import serializers

from .models import FoodItem, FoodNutrient, FoodNutrientInItem


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ("fdcId", "description")


class FoodNutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrient
        fields = ("number", "name")


class FoodNutrientInItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrientInItem
        fields = ("food_item", "food_nutrient", "amount", "unit_name")
