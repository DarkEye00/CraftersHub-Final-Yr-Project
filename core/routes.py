from django.urls import path, include
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
    path("your-products/", views.vendor_products, name="your-products"),
    path("add-products/", views.add_product, name="add-product"),
    # filtr products
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.cart_items, name="cart"),
    path("delete-from-cart/", views.delete_cart_item, name="delete-from-cart"),
    # Adding Reviews
    path("ajax-add-review/<pk>", views.add_review_form, name="ajax-add-review"),
    # Checkout
    path("checkout/", views.checkout_view, name="checkout"),
    # paypal url
    path("paypal/", include("paypal.standard.ipn.urls")),
    # payment successful
    path("payment-completed/", views.payment_completed_view, name="payment_completed"),
    # payment failed
    path("payment-failed/", views.payment_failed_view, name="payment_failed"),
]
