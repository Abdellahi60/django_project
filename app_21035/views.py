# app_21035/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ProductFamily, Product, SellingPoint, Price, Basket, ProductBasket
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404



def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

class ProductFamilyList(ListView):
    model = ProductFamily

class ProductFamilyDetail(DetailView):
    model = ProductFamily  

class ProductFamilyCreate(CreateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('productfamily_list')

class ProductFamilyDelete(DeleteView):
    model = ProductFamily
    success_url = reverse_lazy('productfamily_list')

class ProductFamilyUpdate(UpdateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('productfamily_list')

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class SellingPointList(ListView):
    model = SellingPoint

class SellingPointDetail(DetailView):
    model = SellingPoint

class SellingPointCreate(CreateView):
    model = SellingPoint
    fields = '__all__'
    success_url = reverse_lazy('sellingpoint_list')

class SellingPointDelete(DeleteView):
    model = SellingPoint
    success_url = reverse_lazy('sellingpoint_list')

class SellingPointUpdate(UpdateView):
    model = SellingPoint
    fields = '__all__'
    success_url = reverse_lazy('sellingpoint_list')


class PriceList(ListView):
    model = Price

class PriceDetail(DetailView):
    model = Price

class PriceCreate(CreateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')

class PriceDelete(DeleteView):
    model = Price
    success_url = reverse_lazy('price_list')

class PriceUpdate(UpdateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')

class BasketList(ListView):
    model = Basket

class BasketDetail(DetailView):
    model = Basket

class BasketCreate(CreateView):
    model = Basket
    fields = '__all__'
    success_url = reverse_lazy('basket_list')

class BasketDelete(DeleteView):
    model = Basket
    success_url = reverse_lazy('basket_list')

class BasketUpdate(UpdateView):
    model = Basket
    fields = '__all__'
    success_url = reverse_lazy('basket_list')

class ProductBasketList(ListView):
    model = ProductBasket

class ProductBasketDetail(DetailView):
    model = ProductBasket

class ProductBasketCreate(CreateView):
    model = ProductBasket
    fields = '__all__'
    success_url = reverse_lazy('productbasket_list')

class ProductBasketDelete(DeleteView):
    model = ProductBasket
    success_url = reverse_lazy('productbasket_list')

class ProductBasketUpdate(UpdateView):
    model = ProductBasket
    fields = '__all__'
    success_url = reverse_lazy('productbasket_list')
