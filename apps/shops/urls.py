from django.urls import path
from .views import IndexView, ProductView, AllProductsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('all_products/', AllProductsView.as_view(), name='all products'),
    path('product/<int:pk>/', ProductView.as_view(), name='product')
]
    