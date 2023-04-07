from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name="about"),
    path('product/<str:name>/',views.ProductDetailView.as_view(),name="product_detail"),
    path('cart',views.cart,name='cart')
]