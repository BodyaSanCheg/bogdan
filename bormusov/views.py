from django.shortcuts import render

from .models import *

def get_product(request):
    # возвращает блог всех товаров
    context = Product.objects.all()
    title = 'Товары'
    return render(request, 'bormusov/product.html', {'context':context, 'title':title})


def get_мanufacturer(request):
    # возвращает блог всех производителей
    context = Manufacturer.objects.all()
    title = 'производители'
    return render(request, 'bormusov/manufacturer.html', {'context':context, 'title':title})
