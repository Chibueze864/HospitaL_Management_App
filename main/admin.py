from django.contrib import admin
from main.models import Patient, ItemInventory, StaffInventory

# Register your models here.
admin.site.register(Patient)
admin.site.register(ItemInventory)
admin.site.register(StaffInventory)
