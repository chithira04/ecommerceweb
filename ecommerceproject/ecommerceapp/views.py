from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

def allProductCat(request,cat_slug=None):
    cat_page=None
    products_list=None
    if cat_slug != None:
        cat_page=get_object_or_404(Category,slug=cat_slug)
        products_list=Product.objects.all().filter(category=cat_page,available=True)
        paginator = Paginator(products_list, 6)
    else:
        products_list = Product.objects.all().filter(available=True)
        paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        productsss=paginator.page(page)
    except (EmptyPage,InvalidPage):
        productsss=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'categoryy':cat_page,'products':productsss})

def prodetail(request,cat_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=cat_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'product':product})