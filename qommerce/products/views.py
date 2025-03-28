from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    # Get filter parameters
    category = request.GET.get('category')
    condition = request.GET.get('condition')
    
    # Start with all products
    products = Product.objects.all()
    
    # Apply filters if provided
    if category:
        products = products.filter(category__name=category)
    if condition:
        products = products.filter(condition=condition)
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})