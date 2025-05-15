from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from catalog.views import products_list, products_detail

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.products_list, name='products_list'),
    path('catalog/<int:pk>/', views.products_detail, name='products_detail')
]
