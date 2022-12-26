from django.forms import ModelForm
from main.models import Patient, StaffInventory, ItemInventory
from django import forms
from phonenumber_field.formfields import  PhoneNumberField
from django.core import validators
from datetime import datetime



class PatientForm(forms.Form):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Name",'class': 'form-control',"required":"True"}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={"placeholder":"Email",'class': 'form-control',"required":"True"}))
    message = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Enter Your Message",'class': 'form-control',"required":"True"}))
    date = forms.DateField(label=False,widget=forms.DateInput(attrs={"placeholder":"Set appointment date",'class': 'form-control',"id":"probootstrap-date","required":"True"}))

class StaffMessage(forms.Form):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Name",'class': 'form-control',"required":"True"}))
class StaffForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Name",'class': 'form-control', "required":"True"}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={"placeholder":"Email",'class': ' form-control',"required":"True"}))
    country = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Country","style":"color: #495057",'class': 'form-control',"required":"True"}))
    profile = forms.ImageField(label=False)
    join_date = forms.DateField(label=False,widget=forms.DateInput(attrs={"placeholder":"Join Date","style":"color: #495057",'class': 'form-control',"id":"probootstrap-date","required":"True"}))
    contact = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Phone Number","style":"color: #495057",'class': 'form-control',"required":"True"}))
    class Meta:
        model = StaffInventory
        fields = "__all__"

class InventoryForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Name",'class': 'form-control', "required":"True"}))
    stock = forms.IntegerField(min_value=1)
    item_price = forms.IntegerField(min_value=1)
    item_type = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder":"Item Type","style":"color: #495057",'class': 'form-control',"required":"True"}))
    image = forms.ImageField(label=False)
    date_added = forms.DateField(label=False,widget=forms.DateInput(attrs={"placeholder":"Date Added","style":"color: #495057",'class': 'form-control',"id":"probootstrap-date","required":"True"}))

    class Meta:
        model = ItemInventory
        fields = "__all__"