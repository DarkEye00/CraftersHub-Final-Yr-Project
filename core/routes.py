from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("category/", views.category_list_view, name="category_list"),
]
