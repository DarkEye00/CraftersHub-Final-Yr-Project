# from pyexpat import model
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.utils.html import mark_safe


def user_directory_path(instance, filename):
    """user files uploaded by the vendor will be stored here"""
    return "user_{0}/{1}".format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(
        unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefg123456"
    )
    title = models.CharField(max_length=100, default="food")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image))

    def __str__(self):
        return str(self.title)


class Tags(models.Model):
    pass

    # VENDOR MODEL


class Vendor(models.Model):
    vid = ShortUUIDField(
        unique=True, length=10, max_length=30, prefix="vid", alphabet="abcdefg123456"
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True, blank=True)

    address = models.CharField(max_length=100, default="Nairobi, Kenya")
    contact = models.CharField(max_length=100, default="+254 (712) 345 ")
    rating = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user"
    )

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image))

    def __str__(self):
        return str(self.title)


# MODEL FOR THE ACTUAL PRODUCTS
class Product(models.Model):
    pid = ShortUUIDField(
        unique=True, length=10, max_length=30, prefix="prd", alphabet="abcde345678"
    )
    title = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category"
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, related_name="product"
    )

    image = models.ImageField(upload_to=user_directory_path)

    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=99999, decimal_places=2, default="500")
    old_price = models.DecimalField(max_digits=99999, decimal_places=2, default="2.99")

    specifications = models.TextField(blank=True, null=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    STATUS = (
        ("rejected", "Rejected"),
        ("published", "Published"),
        ("popular", "Popular"),
    )

    product_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review"
    )
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)

    sku = ShortUUIDField(
        unique=True, length=5, max_length=10, prefix="sku", alphabet="12345678"
    )

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image))

    def __str__(self):
        return str(self.title)


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Products Images"


# HANDLING PRODUCT AT THE CART/CART MODEL
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=99999, decimal_places=2, default="1.99")
    payment_status = models.BooleanField(default=False)

    STATUS_CHOICE = (
        ("process", "Product is being Crafted"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    )

    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(
        choices=STATUS_CHOICE, max_length=30, default="processing"
    )

    class Meta:
        verbose_name_plural = "Cart Order"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=200)
    items = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=99999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=999999, decimal_places=2, default="1.99")

    class Meta:
        verbose_name_plural = "CartOrder Items"


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()

    RATING = (
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    )

    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlist"

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"
