from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.index,name="index"),
    path("about_us",views.about,name="about_us"),
    path("contact_us",views.contact_view,name="contact_us"),
    path("prodduct",views.product,name="product"),
    path("parabolic",views.parabolic,name="parabolic"),
    path("trialer_leaf_spring", views.trialer_leaf_spring, name="trialer_leaf_spring"),
    path("conventional_leaf_spring", views.conventional_leaf_spring, name="conventional_leaf_spring"),
    path("erickshaw_leaf_spring", views.erickshaw_leaf_spring, name="erickshaw_leaf_spring"),
    path("truck_leaf_spring", views.truck_leaf_spring, name="truck_leaf_spring"),
]