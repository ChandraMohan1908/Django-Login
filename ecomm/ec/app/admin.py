from django.contrib import admin
from .models import Cart, Product,Customer

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price','category', 'Product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =  ['name', 'locality', 'city', 'mobile', 'zipcod', 'state']

#@admin.register(Cart)
#class CustomerModelAdmin(admin.ModelAdmin):
  #  list_display =  ['id', 'user', 'products', 'quantity']
