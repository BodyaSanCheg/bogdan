from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс редактирования отображения в админке"""

    list_display = ('name', 'product_manufacturer',)
    list_display_links = ('name', 'product_manufacturer',)

admin.site.register(Manufacturer)