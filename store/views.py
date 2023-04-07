from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView
from django.utils.text import slugify
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'store/index.html',{
        'products':products,
    })

def contact(request):
    return render(request,'store/contact.html')

def about(request):
    return render(request,'store/about.html')

class ProductDetailView(DetailView):
    model=Product
    slug_url_kwarg='name'
    slug_field='name'

    queryset=Product.objects.filter()
def cart(request):
    return render(request,'store/cart.html')