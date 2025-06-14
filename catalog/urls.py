from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsView, HomeView, CategoryProductView, CategoryProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='products_list'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='products_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('catalog/category/', CategoryProductView.as_view(), name='category_list'),
    path('catalog/category/<int:pk>/', CategoryProductDetailView.as_view(), name='products_category')
]
