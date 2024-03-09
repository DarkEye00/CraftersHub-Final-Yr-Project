from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

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

'''
def recommend_view(request, pk):

    recommended = content_based_recommendation(pk)

    context = {
        "recomended": recommended,
    }

    return render(request, "core/recommend.html", context)


def content_based_recommendation(pk):
    # Fetch user's preferences or behaviors from the database
    user_preferences = get_user_preferences_from_database(pk)

    # Fetch item data from the database
    products = Product.objects.all()

    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")

    # Use item features as document text for TF-IDF
    item_descriptions = [
        " ".join(
            [
                str(getattr(product, feature))
                for feature in ["title", "description", "category", "price", "status"]
            ]
        )
        for product in products
    ]

    # Debugging information
    print("Length of training data before fitting:", len(item_descriptions))

    # Fit the vectorizer on the item descriptions
    tfidf_vectorizer.fit(item_descriptions)
    tfidf_matrix = tfidf_vectorizer.transform(item_descriptions)
    # Debugging information
    print("Length of training data after fitting:", len(item_descriptions))

    # Compute the cosine similarity between user preferences and item descriptions
    cosine_similarities = linear_kernel(user_preferences, tfidf_matrix).flatten()

    # Get indices of items sorted by similarity
    recommended_indices = cosine_similarities.argsort()[::-1]

    # Get the top N recommended items
    top_n_recommendations = [products[i] for i in recommended_indices[:5]]

    return top_n_recommendations


def get_user_preferences_from_database(pk):
    # Fetch and process user preferences from the database
    # This could include user ratings, likes, etc.
    # For simplicity, let's assume user preferences are a list of features
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")

    user_preferences = get_user_features_from_database(pk)
    return tfidf_vectorizer.transform([" ".join(user_preferences)])


def get_user_features_from_database(pk):
    # Fetch and process user features from the database
    # This could include user preferences, purchase history, etc.
    # For simplicity, let's assume user features are a list of features
    user_features = ["price", "category", "product_status"]
    return user_features
'''