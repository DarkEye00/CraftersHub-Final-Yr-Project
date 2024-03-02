from django.shortcuts import render

# Create your views here.from django.shortcuts import render
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
    """
    This function returns the index page with all products.
    """
    popular = Product.objects.filter(product_status="popular")

    products = Product.objects.all()

    home = Product.objects.filter(category="4", product_status="published")

    furniture = Product.objects.filter(category="5", product_status="published")

    women = Product.objects.filter(category="6", product_status="published")

    # flash = Product.objects.latest()

    context = {
        "popular": popular,
        "products": products,
        "home": home,
        "furniture": furniture,
        "women": women,
    }
    return render(request, "core/index.html", context)


def home_view(request):
    """
    This function returns the index page with all products.
    """
    popular = Product.objects.filter(product_status="popular")

    products = Product.objects.all()

    # flash = Product.objects.latest()

    context = {
        "popular": popular,
        "products": products,
    }
    return render(request, "core/homepage.html", context)


def category_list_view(request):
    """
    This function returns the list of categories.
    """
    category = Category.objects.all()

    context = {"Category": category}

    return render(request, "core/category.html", context)


def category_product_view(request, cid):
    """
    This function returns the list of products in a specific category.
    """
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category=category)

    context = {"category": category, "products": products}

    return render(request, "core/category-product-list.html", context)

    context = {"products": products}
    return render(request, "core/index.html", context)


def category_list_view(request):
    category = Category.objects.all()

    context = {"Category": category}

    return render(request, "core/category.html", context)


""" def category_product_view(request, cid):
     category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category=category)

    context = {"category": category, "products": products}

    return render(request, "core/category-product-list.html", context) """

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    

    context = {"product": product}

    return render(request, "core/product_detail.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()

    context = {
        "vendors": vendors,
    }

    return render(request, "core/vendor-list.html", context)


def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains=query)

    context = {"products": products, "query": query}
    return render(request, "core/search.html", context)
