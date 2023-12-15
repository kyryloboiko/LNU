from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registration(request):  #Registration page
    return render(request, 'user/registration.html')

def authorization(request): #Authorization page
    return render(request, 'user/authorization.html')

def profile(request):   #Profile page
    return render(request, 'user/profile.html')