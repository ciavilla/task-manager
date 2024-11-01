from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("list_projects")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif password != password_confirmation:
                form.add_error(
                    "password_confirmation", "The passwords do not match"
                )
            else:
                user = User.objects.create_user(
                    username=username, password=password
                )
                login(request, user)
                return redirect("list_projects")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def home(request):
    return render(request, 'accounts/home.html')
