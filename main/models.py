from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
# Create your models here.

date = datetime.today()
date_instance = date.date()
class Patient(models.Model):
    name = models.CharField(max_length= 30)
    email = models.CharField(max_length = 30)
    date = models.DateTimeField()
    message = models.TextField(default="")

class ItemInventory(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField(default=0,)
    date_added = models.DateField(default= date_instance)
    item_price = models.IntegerField()
    image = models.ImageField(upload_to="items", default=None)
    item_type = models.CharField(max_length=20)
    in_stock = models.BooleanField(default=True)

class StaffInventory(models.Model):
    name = models.CharField(max_length=35)
    email = models.CharField(max_length= 30)
    country = models.CharField(max_length=30)
    contact = PhoneNumberField(region="NG")
    status = models.BooleanField(default=True)
    profile = models.ImageField(upload_to="staff", default=None)
    join_date = models.DateField(default= date_instance)
