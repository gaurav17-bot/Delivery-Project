from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Customer
from django.contrib import messages
from django.contrib.auth import logout
from .restrict import redirect_if_logged_in,noentry_order


def landing_page(request):
    admin = request.session.get('admin_username')
    username = request.session.get('user_username')
    return render(request, 'app1/landing.html',{'username':username,'admin':admin})

def kausik(request):
    username = request.session.get('user_username')
    return render(request, 'app1/kausik.html',{'username':username})

def chiyaguff(request):
    username = request.session.get('user_username')
    return render(request, 'app1/chiyaguff.html',{'username':username})

def chiyachautari(request):
    username = request.session.get('user_username')
    return render(request, 'app1/chiyachautari.html',{'username':username})


def siddhartha(request):
    username = request.session.get('user_username')
    return render(request, 'app1/siddhartha.html',{'username':username})

def sinka(request):
    username = request.session.get('user_username')
    return render(request, 'app1/sinka.html',{'username':username})


def suva(request):
    username = request.session.get('user_username')
    return render(request, 'app1/suva.html',{'username':username})


def swadghar(request):
    username = request.session.get('user_username')
    return render(request, 'app1/swadghar.html',{'username':username})


def chakatti(request):
    username = request.session.get('user_username')
    return render(request, 'app1/chakatti.html',{'username':username})

@redirect_if_logged_in
def login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Customer.objects.get(email=email,password=password)

            request.session['user_id'] = user.id
            request.session['user_username'] = user.username
            return redirect('landing')
        except Customer.DoesNotExist:
            messages.error(request,'Invalid password or email !') 
            return redirect('login')
        
    return render(request, 'app1/login.html')

@redirect_if_logged_in
def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password = request.POST.get('password')
        confrim_password = request.POST.get('confrim-password')

        if password!=confrim_password:
            messages.error(request,'password didnot match')
            return redirect('register')
        

        customer  = Customer (
            username = username,
            email = email,
            number = number,
            password = password,
        )

        customer.save()
        return redirect('login')
    return render(request, 'app1/register.html')


def logout_view(request):
    request.session.flush()
    return redirect('landing')

@noentry_order
def order(request):
    username = request.session.get('user_username')
    return render(request, 'app1/order.html',{'username':username})
