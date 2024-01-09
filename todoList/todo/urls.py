from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("addtask",views.addtask, name="addtask"),
    path("delete/<int:taskid>",views.delete, name="delete"),
    path("edit/<int:taskid>",views.edit, name="edit"),
    path("register",views.register, name="registerUser"),
    path("login",views.loginUser, name="loginUser "),
    path("logout",views.logoutUser, name="logoutUser "),
    
]
