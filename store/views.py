from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.views.generic import DetailView
from django.utils.text import slugify
from django.urls import reverse

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

def order(request):
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=OrderForm

    return render(request,'store/order.html',{
        'form':form,
    })

def ship(request):
    if request.method == "POST":
        form=AddressForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return reverse('store:index')

    else:
            form=AddressForm
    
    return render(request,'store/address.html',{'form':form})



