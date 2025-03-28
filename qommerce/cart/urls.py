from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
]