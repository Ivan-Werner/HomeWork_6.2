from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(DetailView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
