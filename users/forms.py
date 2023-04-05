from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegisterForm(UserCreationForm):
    
    class Meta():
        model=Profile
        fields="__all__"
        exclude=['USERNAME_FIELD','user']



class UserUpdateForm(forms.ModelForm):
    
    class Meta():
        model=Profile
        fields="__all__"
        exclude=['USERNAME_FIELD']


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['image']
