from django.contrib import admin
from django.urls import path, include
from .views import signup, home,user_logout, custom_login, task, updateTask, deleteTask
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", home, name="home"),
    path("signup/",signup, name='signup'),
    path('user_logout/',user_logout, name='logout_user'),
    path('accounts/',include("django.contrib.auth.urls")),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('task/', task ,name='task'),
    path('update-task/<str:pk>',updateTask,name='update-task'),
    path('delete-task/<str:pk>',deleteTask,name='delete-task'),
]