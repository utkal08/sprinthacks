from django.shortcuts import render
from django.http import HttpResponse
from .models import *
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

def product(request,name):
    return HttpResponse(name)