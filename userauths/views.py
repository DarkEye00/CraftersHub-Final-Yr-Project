from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from userauths.forms import UserRegistrationForm, VendorProfileForm
from userauths.models import User, Group
from core.models import Vendor
from django.contrib.auth.decorators import login_required


# User = settings.AUTH_USER_MODEL


# Create your views here.
def sign_up(request):
    logout(request)

    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():

            user = form.save()
            role = form.cleaned_data["role"]

            if role == User.VENDOR:
                vendor_group, created = Group.objects.get_or_create(name="Vendor")
                user.groups.add(vendor_group)
                user.save()

                username = form.cleaned_data.get("username")
                messages.success(
                    request, f"Hey {username}, Your acccount was created successfully"
                )

                user = authenticate(
                    username=form.cleaned_data["email"],
                    password=form.cleaned_data["password1"],
                )

                login(request, user)

                return redirect("userauths:update-profile")
            else:
                if role == User.CUSTOMER:
                    customer_group, created = Group.objects.get_or_create(
                        name="Customer"
                    )
                    user.groups.add(customer_group)
                    user.save()

                    username = form.cleaned_data.get("username")
                    messages.success(
                        request,
                        f"Hey {username}, Your acccount was created successfully",
                    )

                    user = authenticate(
                        username=form.cleaned_data["email"],
                        password=form.cleaned_data["password1"],
                    )

                    login(request, user)

                    return redirect("core:index")

    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }

    return render(request, "userauths/signup.html", context)


# logging in view


def sign_in(request):
    logout(request)
    # checking if a user is logged in
    if request.user.is_authenticated:
        messages.warning(request, "Your are already logged in")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            # login logic
            user = authenticate(request, email=email, password=password)

            if user is not None:  # user exists in the database
                login(request, user)
                messages.success(request, "Login Successful !")
                return redirect("core:index")

            else:
                messages.warning(
                    request, "Incorrect Password or Username, Create an Account"
                )
        except:
            messages.warning(request, f"User with {email} does not exist")

    context = {}

    return render(request, "userauths/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect("userauths:login")


@login_required
def create_vendor(request):
    # vendor = Vendor.objects.get(user=request.user)

    if request.method == "POST":
        vendor_form = VendorProfileForm(request.POST, request.FILES)

        if vendor_form.is_valid():
            Vendor.objects.create(
                title=vendor_form.cleaned_data["title"],
                image=vendor_form.cleaned_data["image"],
                description=vendor_form.cleaned_data["description"],
                address=vendor_form.cleaned_data["address"],
                contact=vendor_form.cleaned_data["contact"],
                user=request.user,
            )
        
            return redirect("userauths:success")
        else:
            print(vendor_form.errors)
    else:
        vendor_form = VendorProfileForm()

    return render(request, "userauths/vendor-login.html", {"vendor_form": vendor_form})


def success_view(request):
    return render(request, "userauths/success.html")
