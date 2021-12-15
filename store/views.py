from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Product
# Create your views here.
def home(request):
    return(render(request, 'store/index.html'))

def prod(request):
    return(render(request, 'product/product.html'))



class HomeView(ListView):
    model = Product
    template_name = 'store/index.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product.html"

def profile(request):
    return(render(request, 'customer/profile.html'))


def cart(request):
    return(render(request, 'cart/cart.html'))