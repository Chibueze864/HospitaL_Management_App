from django.urls import path
from main import views
app_name="main"

urlpatterns= [
    path("patient/<int:pk>", views.patients, name = "add_patient"),
    path("", views.home, name="home"),
    path("inventory/<int:pk>", views.inventory, name="inventory"),
    path("delete_item/<int:id>", views.delete_item, name="delete_item"),

    path("staff/<int:pk>", views.staff, name="inventory"),
    path("delete_staff/<int:id>", views.delete_staff, name="delete_staff"),
    path("delete_patient/<int:id>", views.delete_patient, name="delete_patient"),
    path("message_staff/<str:email>", views.message_staff, name="message_staff"),

]