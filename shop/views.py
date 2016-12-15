from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def register(request):
    return render(request, 'shop/register.html')


def store(request):
    return render(request, 'shop/store.html')


def cart(request):
    return render(request, 'shop/cart.html')

def deals(request):
    return render(request, 'shop/deals.html')



