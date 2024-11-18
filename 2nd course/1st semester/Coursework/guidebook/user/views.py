from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, 'authentication/login.html')
    else:
        return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/registration.html', {'form': form})

def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})
