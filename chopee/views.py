from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'chopee/home.html')
def product_create(request):
    p = product(
            name = "Lv",
            brand = "Gucci-Bag",
            price = 40000,
            year = 2020 ,       
        )
    p.save()
    return render(request, 'chopee/product/create.html')
def product_read(request):
    return render(request, 'chopee/product/read.html')
def product_update(request):
    return render(request, 'chopee/product/update.html')
def product_delete(request):
    return render(request, 'chopee/product/delete.html')
def product_list(request):
    return render(request,'chopee/product/list.html')