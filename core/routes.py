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
    path("product-detail/<pk>/", views.product_detail_view, name="details"),
    # search
    path("search/", views.search_view, name="search"),
    # path("recommend/<pk>/", views.recommend_view, name="recommend"),
    path("add-products/", views.add_product, name="add-product"),
]
