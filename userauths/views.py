from django.shortcuts import render, redirect
from userauths.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def sign_up(request):
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your acccount was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password = form.cleaned_data['password1']         
                                    )
            
            login(request, new_user)
            return redirect("core:index")
            


    else: 
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, "userauths/signup.html", context)

def login(request):
    return render (request, "userauths/login.html")


