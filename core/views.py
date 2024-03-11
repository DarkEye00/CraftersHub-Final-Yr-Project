from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import ProductForm
from django.contrib import messages


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

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

    furniture = Product.objects.filter(category="5", product_status="in_stock")

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


def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)

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
    # key = Product.objects.get(pk=pk)

    products = Product.objects.filter(title__icontains=query)
    # recommended = content_based_recommendation(key)

    context = {
        "products": products,
        "query": query,
        # "recommended": recommended,
    }
    return render(request, "core/search.html", context)


@login_required
def add_product(request):
    vendor = Vendor.objects.get(user=request.user)
    categories = Category.objects.all()

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            # Retrieve or create the Category instance
            category_name = product_form.cleaned_data["category"]
            category, created = Category.objects.get_or_create(title=category_name)

            # Create a new Product instance with the associated Category
            Product.objects.create(
                title=product_form.cleaned_data["title"],
                description=product_form.cleaned_data["description"],
                price=product_form.cleaned_data["price"],
                specifications=product_form.cleaned_data["specifications"],
                image=product_form.cleaned_data["image"],
                product_status=product_form.cleaned_data["product_status"],
                category=category,
                vendor=vendor,
                user=request.user,
            )
        messages.success(request, "Product added successfully")
        return redirect("userauths:profile")
    else:
        product_form = ProductForm()

    return render(
        request,
        "core/add_product.html",
        {"product_form": product_form, "categories": categories},
    )
