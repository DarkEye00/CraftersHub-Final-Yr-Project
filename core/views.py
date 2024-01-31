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

    context = {"products": products}
    return render(request, "core/index.html", context)


def category_list_view(request):
    category = Category.objects.all()

    context = {"Category": category}

    return render(request, "core/category.html", context)


def category_product_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category=category)

    context = {"category": category, "products": products}

    return render(request, "core/category-product-list.html", context)
