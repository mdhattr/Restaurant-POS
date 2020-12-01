from django.shortcuts import render, redirect
from .models import Ingredient, Entree, Side, IngredientInEntree, IngredientInSide, Table, FoodForTable, DayStats

def index(request):
    context={
        'Table':Table.objects.all(),
        'Entree':Entree.objects.all(),
        'Side':Side.objects.all(),
        'DayStats':DayStats.objects.get(id=1)
    }
    return render(request, 'index.html', context)

def order_food(request):
    FoodForTable.objects.create(table_id=request.POST['table'], entree_id=request.POST['entree'], side_id=request.POST['side'])
    c = Table.objects.get(id=request.POST['table'])
    c.bill_amount += Entree.objects.get(id=request.POST['entree']).menu_price+Side.objects.get(id=request.POST['side']).menu_price
    c.save()
    d=DayStats.objects.get(id=1)
    d.total_sales+=c.bill_amount
    d.meals_served+=1
    d.save()
    return redirect('/')

def view_receipt(request, id):
    context={
        'Receipt':FoodForTable.objects.filter(table_id=id),
        'Table':Table.objects.get(id=id)
    }
    return render(request, 'receipt.html', context)