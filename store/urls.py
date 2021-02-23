from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkOut, name='checkout'),
    path('cart/', views.cart, name='cart'),
]
