from django.contrib import admin
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


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]


class VendorAdmin(admin.ModelAdmin):
    list_display = ["title", "vendor_image", "user"]


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "payment_status", "order_date", "product_status"]


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "invoice_no",
        "items",
        "product_status",
        "qty",
        "image",
        "price",
        "total",
    ]


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]


class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]


class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"]


class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = [
        "user",
        "title",
        "product_image",
        "category",
        "price",
        "product_status",
        "pid",
    ]


admin.site.register(Product, ProductsAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
