from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'chopee/home.html')

def product_create(request):
    if request.method == 'GET':
        # ส่งหน้าฟอร์มเปล่า ๆ ให้ผู้ใช้กรอก
        return render(request, 'chopee/product/create.html')
        
    elif request.method == 'POST':
        # บันทึกข้อมูลเมื่อผู้ใช้กด Submit ส่งฟอร์มเข้ามา
        p = product(
            name = "Lv",
            brand = "Gucci-Bag",
            price = 40000,
            year = 2020,       
        )
        p.save()
        # เมื่อบันทึกเสร็จ สามารถส่งกลับไปหน้าเดิม หรือใช้ redirect ไปหน้า list ก็ได้ครับ
        return render(request, 'chopee/product/create.html')
def product_read(request):
    return render(request, 'chopee/product/read.html')
def product_update(request):
    return render(request, 'chopee/product/update.html')
def product_delete(request):
    return render(request, 'chopee/product/delete.html')
def product_list(request):
    return render(request,'chopee/product/list.html')