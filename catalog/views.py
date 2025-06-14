from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.services import get_products_by_category_from_cache, CategoryService


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product

    # def get_queryset(self):
    #     if self.request.user.groups.filter(name='moderator').exists():
    #         # Если пользователь является модератором, возвращаем все продукты
    #         return Product.objects.all()
    #     elif self.request.user.is_authenticated:
    #         # Иначе, если пользователь аутентифицирован, показываем только его продукты
    #         return Product.objects.filter(owner=self.request.user)
    #     return Product.objects.none()

    def get_queryset(self):
        return get_products_by_category_from_cache(self.request.user)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return ProductForm
        if self.request.user.has_perm('can_unpublish_product'):
            return ProductModeratorForm
        if self.request.user.has_perm('can_delete_product'):
            return ProductModeratorForm
        return ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def delete_product(request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if request.user == product.owner:
            product.delete()
            return redirect('product_list')
        else:
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")


class CategoryProductView(ListView):
    model = Category
    template_name = 'catalog/products_category.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryProductDetailView(DetailView):
    model = Category
    template_name = 'catalog/products_in_category.html'

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data(**kwargs)
        # Получаем ID категория из объекта
        category_id = self.kwargs.get('pk')
        context['category_id'] = category_id
        context['name'] = CategoryService.get_category_name(category_id)
        context['products'] = Product.objects.filter(category_id=category_id)
        print(context['products'])
        return context





