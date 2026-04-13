from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .models import FoodItem, Order, OrderItem


def landing_page(request):
    return render(request, 'app1/landing.html')


def kausik(request):
    items = FoodItem.objects.all()
    return render(request, 'app1/kausik.html', {'items': items})


def chiyaguff(request):
    return render(request, 'app1/chiyaguff.html')


def chiyachautari(request):
    return render(request, 'app1/chiyachautari.html')


def siddhartha(request):
    return render(request, 'app1/siddhartha.html')


def sinka(request):
    return render(request, 'app1/sinka.html')


def suva(request):
    return render(request, 'app1/suva.html')


def swadghar(request):
    return render(request, 'app1/swadghar.html')


def chakatti(request):
    return render(request, 'app1/chakatti.html')



# cart showing
from django.http import JsonResponse

from django.http import JsonResponse

def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart

    return JsonResponse({
        'status': 'success',
        'message': 'Item added to cart!'
    })


# cart items
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for id, qty in cart.items():
        food = FoodItem.objects.get(id=id)
        total += food.price * qty
        items.append({
            'food':food,
            'qty':qty
          })

    return render(request, 'app1/cart.html', {
        'items':items,
        'total':total
       })


# for upadting cart
def update_cart(request, id, action):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        if action == 'add':
            cart[str(id)] += 1
        elif action =='remove':
            cart[str(id)] -= 1

        if cart[str(id)] <= 0:
            del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')


# its checkout section
def checkout(request):
    cart = request.session.get('cart', {})
    total = 0

    order = Order.objects.create(total_price=0)

    for id, qty in cart.items():
        food = FoodItem.objects.get(id=id)
        total += food.price * qty

        OrderItem.objects.create(
            order=order,
            food_item=food,
            quantity=qty
       )

    order.total_price = total
    order.save()

    request.session['cart'] = {}

    return render(request, 'app1/sucess.html', {'order': order})