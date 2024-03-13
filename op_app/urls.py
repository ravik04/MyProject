from django.contrib import admin
from django.urls import path
from op_app import views

urlpatterns = [
    path("",views.index ,name='home' ),

]
