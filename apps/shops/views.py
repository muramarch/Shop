from django.shortcuts import render
from django.views import View

from apps.shops.serializers import CategorySerializer, ProductSerializer, SpecificationSerializer
from .models import Product, Category, Specification
from rest_framework import generics

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shops/index.html', {'products': products})
    
    
class ProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'shops/product.html', {'product': product})
    
    
class AllProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shops/all_products.html', {'products': products})
    
    
class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class SpecificationView(generics.ListAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer