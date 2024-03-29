from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import ProductForm, ProductReviewForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Avg

from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

# from core.recommender import ContentBasedRecommender


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

    home = Product.objects.filter(category="3", product_status="in_stock")

    paint = Product.objects.filter(category="5", product_status="in_stock")

    furniture = Product.objects.filter(category="4", product_status="in_stock")

    women = Product.objects.filter(category="6", product_status="in_stock")

    # flash = Product.objects.latest()

    context = {
        "popular": popular,
        "products": products,
        "home": home,
        "furniture": furniture,
        "women": women,
        "paint": paint,
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

    # getting all product reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Average ratings for specific product
    average_rating = ProductReview.objects.filter(product=product).aggregate(
        rating=Avg("rating")
    )

    # product review_form
    review_form = ProductReviewForm()

    context = {
        "product": product,
        "reviews": reviews,
        "average_rating": average_rating,
        "review_form": review_form,
    }

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

    context = {
        "products": products,
        "query": query,
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


@login_required
def vendor_products(request):
    user = request.user
    vendor = Vendor.objects.get(user=user)

    products = Product.objects.filter(vendor=vendor)

    context = {"user": user, "vendor": vendor, "products": products}

    return render(request, "core/view_products.html", context)


def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET["id"])] = {
        "title": request.GET["title"],
        "qty": request.GET["qty"],
        "image": request.GET["image"],
        "price": request.GET["price"],
        "pid": request.GET["pid"],
    }
    if "cart_data_obj" in request.session:
        if str(request.GET["id"]) in request.session["cart_data_obj"]:
            cart_data = request.session["cart_data_obj"]
            cart_data[str(request.GET["id"])]["qty"] = int(
                cart_product[str(request.GET["id"])]["qty"]
            )
            cart_data.update(cart_data)
            request.session["cart_data_obj"] = cart_data
        else:
            cart_data = request.session["cart_data_obj"]
            cart_data.update(cart_product)
            request.session["cart_data_obj"] = cart_data
    else:
        request.session["cart_data_obj"] = cart_product

    return JsonResponse(
        {
            "data": request.session["cart_data_obj"],
            "totalcartitems": len(request.session["cart_data_obj"]),
        }
    )


def cart_items(request):

    cart_total_amount = 0

    if "cart_data_obj" in request.session:
        for p_id, item in request.session["cart_data_obj"].items():
            cart_total_amount += int(item["qty"]) * float(item["price"])

        return render(
            request,
            "core/cart.html",
            {
                "cart_data": request.session["cart_data_obj"],
                "totalcartitems": len(request.session["cart_data_obj"]),
                "cart_total_amount": cart_total_amount,
            },
        )
    else:
        messages.warning(request, "Your cart is Empty")
        return redirect("core:index")


def delete_cart_item(request):
    product_id = str(request.GET["id"])

    if "cart_data_obj" in request.session:
        if product_id in request.session["cart_data_obj"]:
            cart_data = request.session["cart_data_obj"]
            del request.session["cart_data_obj"][product_id]
            request.session["cart_data_obj"] = cart_data

    cart_total_amount = 0

    if "cart_data_obj" in request.session:
        for p_id, item in request.session["cart_data_obj"].items():
            cart_total_amount += int(item["qty"]) * float(item["price"])

    context = render_to_string(
        "core/async/cart-list.html",
        {
            "cart_data": request.session["cart_data_obj"],
            "totalcartitems": len(request.session["cart_data_obj"]),
            "cart_total_amount": cart_total_amount,
        },
    )
    return JsonResponse(
        {"data": context, "totalcartitems": len(request.session["cart_data_obj"])}
    )


def add_review_form(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST["review"],
        rating=request.POST["rating"],
    )
    context = {
        "user": user.username,
        "review": request.POST["review"],
        "rating": request.POST["rating"],
    }
    average_reviews = ProductReview.objects.filter(product=product).aggregate(
        rating=Avg("rating")
    )

    return JsonResponse(
        {
            "bool": True,
            "context": context,
            "average_review": average_reviews,
        }
    )


@login_required
def checkout_view(request):
    host = request.get_host()
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "200",
        "item_name": "Order-item-15",
        "invoice": "INVOICE 15",
        "currency_code": "USD",
        "return_url": "https://{}{}".format(host, reverse("core:payment_completed")),
        "cancel_url": "https://{}{}".format(host, reverse("core:payment_failed")),
    }

    paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

    cart_total_amount = 0

    if "cart_data_obj" in request.session:
        for p_id, item in request.session["cart_data_obj"].items():
            cart_total_amount += int(item["qty"]) * float(item["price"])

        return render(
            request,
            "core/checkout.html",
            {
                "cart_data": request.session["cart_data_obj"],
                "totalcartitems": len(request.session["cart_data_obj"]),
                "cart_total_amount": cart_total_amount,
                "paypal_payment_button": paypal_payment_button,
            },
        )
    else:
        return redirect("core:cart")


"""def detail(request, pk):
    # Get recommendations for the specified product
    recommendations = recommend_similar_products(pk=pk)

    context = {
        "recommendations": recommendations,
    }
    return render(request, "core/detail.html", context)

def recommend_products(request, pid):
    recommender = ContentBasedRecommender()
    recommender.fit()
    recommendations = recommender.recommend(pid)
    recommended_product_ids = [rec[0] for rec in recommendations]
    recommended_products = Product.objects.filter(pid__in=recommended_product_ids)
    context = {"recommended_products": recommended_products}
    return render(request, "recommendations.html", context) """


def payment_completed_view(request):
    return render(request, "core/payment_completed.html")


def payment_failed_view(request):
    return render(request, "core/payment_failed.html")
