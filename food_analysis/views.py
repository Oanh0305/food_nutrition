from django.http import HttpResponse

from .models import FoodItem, FoodNutrient, FoodNutrientInItem
from rest_framework import viewsets
from .serializers import (
    FoodItemSerializer,
    FoodNutrientSerializer,
    FoodNutrientInItemSerializer,
)


class FoodNutrientInItemView(viewsets.ModelViewSet):
    serializer_class = FoodNutrientInItemSerializer
    queryset = FoodNutrientInItem.objects.all()

class FoodItemView(viewsets.ModelViewSet):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()


class FoodNutrientView(viewsets.ModelViewSet):
    serializer_class = FoodNutrientSerializer
    queryset = FoodNutrient.objects.all()
