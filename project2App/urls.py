from django.urls import path
from . import views
from .models import Ingredient, Entree, Side, IngredientInEntree, IngredientInSide, Table, FoodForTable, DayStats

urlpatterns=[
    path('', views.index),
    path('order_food', views.order_food),
    path('view_receipt/<int:id>', views.view_receipt),
]