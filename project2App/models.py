from django.db import models

class Ingredient(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    quantity_in_fridge=models.IntegerField()
    portion_per_case=models.IntegerField()
    price_per_case=models.IntegerField()

class Entree(models.Model):
    name=models.CharField(max_length=255)
    menu_price=models.IntegerField()

class Side(models.Model):
    name=models.CharField(max_length=255)
    menu_price=models.IntegerField()

class IngredientInEntree(models.Model):
    entree=models.ForeignKey(Entree, related_name='ingredient_in_entree', on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient, related_name='ingredient_in_entree', on_delete=models.CASCADE)

class IngredientInSide(models.Model):
    side=models.ForeignKey(Side, related_name='ingredient_in_side', on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient, related_name='ingredient_in_side', on_delete=models.CASCADE)

class Table(models.Model):
    number=models.IntegerField()
    bill_amount=models.IntegerField()
    
class FoodForTable(models.Model):
    table=models.ForeignKey(Table, related_name='food_for_table', on_delete=models.CASCADE)
    entree=models.ForeignKey(Entree, related_name='food_for_table', on_delete=models.CASCADE)
    side=models.ForeignKey(Side, related_name='food_for_table', on_delete=models.CASCADE)

class DayStats(models.Model):
    total_sales=models.IntegerField()
    total_food_cost=models.IntegerField()
    tables_sat=models.IntegerField()
    meals_served=models.IntegerField()
# Create your models here.
