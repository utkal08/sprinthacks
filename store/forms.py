from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import *

class OrderForm(forms.ModelForm):
    
    class Meta():
        model=OrderItem
        fields='__all__'
        exclude=['order']

class AddressForm(forms.ModelForm):

    class Meta():
        model=ShippingAddress
        fields=['address','city','state','pincode']
        
