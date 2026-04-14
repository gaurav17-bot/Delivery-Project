# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.landing_page, name='landing'),
#     path('kausik/', views.kausik, name='kausik'),
#     path('chiyaguff/', views.chiyaguff, name='chiyaguff'),
#     path('chiyachautari/', views.chiyachautari, name='chiyachautari'),
#     path('siddhartha/', views.siddhartha, name='siddhartha'),
#     path('sinka/', views.sinka, name='sinka'),
#     path('suva/', views.suva, name='suva'),
#     path('swadghar/', views.swadghar, name='swadghar'),
#     path('chakatti/', views.chakatti, name='chakatti'),

#     # cart system
#     path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.cart_view, name='cart'),
#     path('update-cart/<int:id>/<str:action>/', views.update_cart, name='update_cart'),
#     path('checkout/', views.checkout, name='checkout'),

#     # auth
#     path('login/', views.login, name='login'),
#     path('register/', views.register, name='register'),
#     path('logout/', views.logout_view, name='logout'),

#     path('order/', views.order, name='order'),

#     path('hotel/<slug:slug>/', views.hotel_detail, name='hotel_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Main Landing Page
    path('', views.landing_page, name='landing'),

    # Cart System
    # Note: Ensure views.add_to_cart returns JsonResponse for your JS to work!
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('update-cart/<int:id>/<str:action>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Authentication
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Orders
    path('order/', views.order, name='order'),

    # Dynamic Hotel Router
    # This replaces kausik/, sinka/, etc. 
    # It will automatically find 'app1/kausik.html' if the slug is 'kausik'
    path('hotel/<slug:slug>/', views.hotel_detail, name='hotel_detail'),
]