from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from main.forms import PatientForm, StaffForm, InventoryForm
from main.models import Patient, ItemInventory, StaffInventory
from django.contrib import messages
from datetime import datetime
import math
from django.core.mail import send_mail

def home(request):
    return render(request,"index.html ")

def inventory(request,pk):
        if request.method == "POST":
            form = InventoryForm(request.POST, request.FILES)
            if form.is_valid():
                                    
                form.save()
                return HttpResponseRedirect(str(pk))
            else: 
                messages.info(request,"Invalid data")
                return HttpResponseRedirect(str(pk))
        else:
             
            form = InventoryForm()
            item_count = len(ItemInventory.objects.all())
            start = pk * 5
            stopp = 5 * (pk+1)
            items = ItemInventory.objects.all()[start:stopp]
            tabs_no = math.ceil(item_count / 5)
            context = {"tab": pk + 1,"tab_count":tabs_no,"pk": pk,"items":items,"count": item_count,"list_count": stopp, "form":form,"tabs": range(1,tabs_no+1)}
            return render(request,"inventory.html", context)
            
def delete_item(request,id):
    item = ItemInventory.objects.get(id=id)
    item.delete()
    return redirect("/inventory/0")

def staff(request,pk):
    if request.method == "POST":
            form = StaffForm(request.POST, request.FILES)
            if form.is_valid():
                                    
                form.save()
                return HttpResponseRedirect(str(pk))
            else: 
                messages.info(request,"Invalid data")
                return HttpResponseRedirect(str(pk))
            
    else:
             
            staff = StaffInventory()
            form = StaffForm()
            staff_count = len(StaffInventory.objects.all())
            start = pk * 5
            stopp = 5 * (pk+1)
            staff = StaffInventory.objects.all()[start:stopp]
            tabs_no = math.ceil(staff_count / 5)
            context = {"tab": pk + 1,"tab_count":tabs_no,"pk": pk,"staff":staff,"count": staff_count,"list_count": stopp, "form":form,"tabs": range(1,tabs_no+1)}
            return render(request,"staff.html", context)

def message_staff(request, email):
    if request.method == "POST":
        sender = request.user.email
        message = request.POST["mail"]
        send_mail("Hospital Message",message, sender, recipient_list=[email])
        return render(request,"message_staff.html",{"mail":email})
    else:
        return render(request,"message_staff.html",{"mail":email})

        
def delete_staff(request,id):
    staff = StaffInventory.objects.get(id=id)
    staff.delete()
    return redirect("/staff/0")

def patients(request,pk):
    if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data["email"]
                date = form.cleaned_data['date']     
                message = form.cleaned_data["message"]       
                patient = Patient(name=name,email=email,date=date, message=message)
                patient.save()
                messages.info(request,"Patient successfully added")

                return HttpResponseRedirect(str(pk))
            else: 
                messages.info(request,"Invalid data")
                return HttpResponseRedirect(str(pk))
            
    else:
        patient_count = len(Patient.objects.all())
        start = pk * 5
        stopp = 5 * (pk+1)
        patients = Patient.objects.all()[start:stopp]
        tabs_no = math.ceil(patient_count / 5)
        date = datetime.today()
        date_instance = date.date()
        date = PatientForm()
        context = {"tab_count":tabs_no,"pk": pk,'date': date_instance, "start": start,"tab": pk + 1, "list_count": stopp  , "form":date,"count":patient_count, "patients":patients,"tabs": range(1,tabs_no+1)}

        return render(request,"patient.html", context)

def delete_patient(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect("/patient/0")
