from django.urls import path
from userauths import views

app_name= "userauths"

urlpatterns = [
    path("Register/", views.sign_up, name='register'),
    path("Login/cd", views.login, name='login')
] 
