from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('kausik/', views.kausik, name='kausik'),
    path('chiyaguff/', views.chiyaguff, name='chiyaguff'),
    path('chiyachautari/', views.chiyachautari, name='chiyachautari'),
    path('siddhartha/', views.siddhartha, name='siddhartha'),
    path('sinka/', views.sinka, name='sinka'),
    path('suva/', views.suva, name='suva'),
    path('swadghar/', views.swadghar, name='swadghar'),
    path('chakatti/', views.chakatti, name='chakatti'),
#  this is ordering part
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('update-cart/<int:id>/<str:action>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
]