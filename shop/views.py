from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Item


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        email_confirm = request.POST['email_confirm']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        errors = validate(username, email, email_confirm, password, password_confirm)
        if errors is None:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('shop:index')
        else:
            # used to refill registration form with previously inputted data
            data = {'username': username, 'email': email, 'email_confirm': email_confirm}
            return render(request, 'shop/register.html', {'errors': errors, 'data': data})

    return render(request, 'shop/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('shop:index')
        else:
            context = {'error_message': 'Username or password are incorrect', 'username': username}
            return render(request, 'shop/index.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def logout_user(request):
    logout(request)
    return redirect('shop:index')


def validate(username, email, email_confirm, password, password_confirm):

    errors = {'username_error': None,
              'email_error': None,
              'email_confirm_error': None,
              'password_error': None,
              'password_confirm_error': None}

    if not username:
        errors['username_error'] = 'Username field cannot be blank.'

    if not email:
        errors['email_error'] = 'Email field cannot be blank.'

    if not email_confirm:
        errors['email_confirm_error'] = 'Confirm email field cannot be blank.'

    if email != email_confirm:
        errors['email_confirm_error'] = 'Email and confirm email fields do not match.'

    if not password:
        errors['password_error'] = 'Password field cannot be blank.'

    if not password_confirm:
        errors['password_confirm_error'] = 'Confirm password field cannot be blank.'

    if password != password_confirm:
        errors['password_confirm_error'] = 'Password and confirm password fields do not match.'

    for key, value in errors.items():
        if value is None:
            continue
        else:
            return errors

    return None


def store(request):
    items = Item.objects.all()
    return render(request, 'shop/store.html', {'items': items})


def cart(request):
    return render(request, 'shop/cart.html')

def deals(request):
    items = Item.objects.filter(sale=True)
    return render(request, 'shop/deals.html', {'items': items})



