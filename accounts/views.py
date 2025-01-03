from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import UserProfile
from django.contrib.auth.models import User

def users_index(request):
    return render(request, "templates/users_index.html", {"users": UserProfile.objects.all()})

def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "templates/user_profile.html", {"user": request.user})
    else:
        return redirect("HomePage")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("HomePage")
        else:
            return render(request, "templates/login.html", {"error": "Invalid credentials"})

    return render(request, "templates/login.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        email = request.POST["email"]

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                return redirect("HomePage")
            except Exception as e:
                return render(request, "templates/signup.html", {"error": str(e)})
        else:
            return render(request, "templates/signup.html", {"error": "Passwords do not match"})

    return render(request, "templates/signup.html")

def logout_view(request):
    logout(request)
    return redirect("HomePage")
