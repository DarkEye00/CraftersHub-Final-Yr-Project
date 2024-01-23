from django.shortcuts import render
from core.models import (
    ProductImages,
    Product,
    CartOrder,
    Address,
    Vendor,
    ProductReview,
    Category,
    CartOrderItems,
    Wishlist,
)


# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {"Product": products}
    return render(request, "core/index.html", context)


def cart(request):
    return render(request, "cart.html")
