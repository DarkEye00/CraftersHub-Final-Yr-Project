from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("welcome/", views.index, name="index"),
    # category
    path("category/", views.category_list_view, name="category-list"),
    path("category/<cid>/", views.category_product_view, name="category-product-list"),
    # vendor
    path("vendors/", views.vendor_list_view, name="vendor-list"),
    path("product-detail/<pid>", views.product_detail_view, name="product-details"),
    # search
    path("search/", views.search_view, name="search"),
]
