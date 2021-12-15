from django.urls import path
from .views import HomeView, ProductDetailView, profile, cart

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('profile/', profile),
    path('cart/', cart)
]
