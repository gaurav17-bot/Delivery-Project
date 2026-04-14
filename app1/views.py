from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .models import FoodItem, Order, OrderItem, Customer,Hotel
from .restrict import redirect_if_logged_in, noentry_order


def landing_page(request):
    hotels = Hotel.objects.all()
    return render(request, 'app1/landing.html', {'hotels': hotels})


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


# ------------------ CART SYSTEM ------------------

def add_to_cart(request, id):
    # Check if custom session user_id exists
    if not request.session.get('user_id'):
        return JsonResponse({
            'status': 'error', 
            'message': 'Please login first',
            'redirect_url': '/login/' # or use reverse('login')
        }, status=401)

    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return JsonResponse({'status': 'success', 'message': 'Item added to cart!'})

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for id, qty in cart.items():
        food = FoodItem.objects.get(id=id)
        total += food.price * qty

        items.append({
            'food': food,
            'qty': qty
        })

    return render(request, 'app1/cart.html', {
        'items': items,
        'total': total
    })


from django.urls import reverse

def update_cart(request, id, action):
    # 1. Check if user is logged in (using your session-based auth)
    if not request.session.get('user_id'):
        messages.info(request, "Please log in to manage your cart.")
        return redirect('login')

    # 2. Get the current cart from session
    cart = request.session.get('cart', {})
    item_id = str(id)

    # 3. Handle Add/Remove logic
    if item_id in cart:
        if action == 'add':
            cart[item_id] += 1
        elif action == 'remove':
            cart[item_id] -= 1
        
        # Remove item entirely if quantity hits zero
        if cart[item_id] <= 0:
            del cart[item_id]
    else:
        # If the item isn't in the cart yet, only 'add' makes sense
        if action == 'add':
            cart[item_id] = 1

    # 4. Save the updated cart back to session
    request.session['cart'] = cart
    
    # 5. Redirect back to the cart page
    # Adding f'#item-{id}' helps the browser jump back to the specific row
    return redirect(reverse('cart') + f'#item-{id}')


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


# ------------------ AUTH SYSTEM ------------------

@redirect_if_logged_in
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Customer.objects.get(email=email, password=password)

            request.session['user_id'] = user.id
            request.session['user_username'] = user.username

            return redirect('landing')

        except Customer.DoesNotExist:
            messages.error(request, 'Invalid email or password!')
            return redirect('login')

    return render(request, 'app1/login.html')


@redirect_if_logged_in
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confrim-password')

        if password != confirm_password:
            messages.error(request, 'Password did not match')
            return redirect('register')

        customer = Customer(
            username=username,
            email=email,
            number=number,
            password=password,
        )
        customer.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'app1/register.html')


def logout_view(request):
    request.session.flush()
    return redirect('landing')


@noentry_order
def order(request):
    username = request.session.get('user_username')
    return render(request, 'app1/order.html', {'username': username})


# for hotels entry
def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'app1/home.html', {'hotels': hotels})

def hotel_detail(request, slug):
    try:
        hotel = Hotel.objects.get(slug=slug)
        # Filter food so ONLY this hotel's food shows up
        items = FoodItem.objects.filter(hotel=hotel)
        
        # This looks for 'kausik.html' if the slug is 'kausik'
        template_name = f'app1/{slug}.html' 
        
        return render(request, template_name, {
            'hotel': hotel,
            'items': items,
            'username': request.session.get('user_username'),
        })
    except Hotel.DoesNotExist:
        return render(request, 'app1/404.html', status=404)