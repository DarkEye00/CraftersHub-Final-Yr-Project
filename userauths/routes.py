from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.sign_up, name="register"),
    path("sign-in/", views.sign_in, name="login"),
    path("sign-out/", views.logout_view, name="logout"),
    path("update_profile/", views.create_vendor, name="update-profile"),
    path("vendor_profile/", views.success_view, name="profile"),
]
