from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


@login_required
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, in_stock=True)
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'products/category.html', context=context)


@login_required
def product_all(request):
    products = Product.products.all()
    context = {
        'products': products,
    }
    return render(request, 'store/home.html', context=context)


@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product': product}
    return render(request, 'products/single.html', context=context)
