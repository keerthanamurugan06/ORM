from django.db import models
from django.contrib import admin
class Product (models.Model):
    Product_code=models.CharField(primary_key=True, max_length=7)
    Name_of_product=models.CharField(max_length=10)
    Categories=models.CharField(max_length=10)
    Rate=models.IntegerField(max_length=10)
    Manufacture_date=models.DateTimeField()
    Expiredate=models.DateField()
    Discount_of_product=models.IntegerField(max_length=2)
class ProductAdmin(admin.ModelAdmin):
    list_display=["Product_code","Name_of_product","Categories","Rate","Manufacture_date","Expiredate","Discount_of_product"]
