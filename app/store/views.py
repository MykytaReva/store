from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories(request):
    return {'categories': Category.objects.all(), }


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, in_stock=True)
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'products/category.html', context=context)


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/home.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product': product}
    return render(request, 'products/detail.html', context=context)
