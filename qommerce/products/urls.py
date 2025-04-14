# products/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('<int:pk>/', views.product_detail, name='product_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]