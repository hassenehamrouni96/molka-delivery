from django.contrib import admin
from .models import Order
from .models import Product
admin.site.register(Order)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
