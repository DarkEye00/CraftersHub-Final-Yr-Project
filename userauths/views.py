from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from userauths.forms import UserRegistrationForm
from userauths.models import User


# User = settings.AUTH_USER_MODEL


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hey {username}, Your acccount was created successfully"
            )
            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )

            login(request, new_user)

            return redirect("core:index")

    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }

    return render(request, "userauths/signup.html", context)


# logging in view


def sign_in(request):
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
