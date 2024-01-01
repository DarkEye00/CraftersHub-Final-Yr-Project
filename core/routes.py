from django.urls import path
from core import views

app_name= "core"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("cart/", views.cart)
]