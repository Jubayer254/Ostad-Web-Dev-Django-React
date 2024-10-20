from django.shortcuts import render
from .models import Product, Category
from django.db.models import Avg, Count

# Create your views here.

# def index(request):

#     products = Product.objects.all().order_by('price')
#     # products = Product.objects.all().order_by('-price', 'title')[:2]
#     # products = Product.objects.raw('SELECT * FROM PRODUCTS_PRODUCT')


#     # category = Category.objects.all().order_by('title')
#     categories = Category.objects.all().order_by('title').annotate(product_count=Count("product"))
    
#     avg_price = products.aggregate(Avg("price"))["price__avg"]

#     return render(request, 'products/index.html', {"products": products, "categories": categories, "avg_price": avg_price})

def index(request):
    
    products = Product.objects.all().order_by('price').select_related('category')

    categories = Category.objects.all().order_by('title').annotate(product_count=Count("product")).prefetch_related("product_set")
    
    avg_price = products.aggregate(Avg("price"))["price__avg"]

    return render(request, 'products/index.html', {"products": products, "categories": categories, "avg_price": avg_price})