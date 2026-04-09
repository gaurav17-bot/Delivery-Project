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
    path('chakatti/', views.swadghar, name='chakatti'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.logout_view, name='logout'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    path('order/',views.order,name='order'),
]