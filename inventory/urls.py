from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_products/', views.generate_products, name='generate_products'),
    path('sort_asc/', views.sort_asc, name='sort_asc'),
    path('sort_desc/', views.sort_desc, name='sort_desc'),
    path('reduce_stock/', views.reduce_stock, name='reduce_stock'),
    path('update_even_stock/', views.update_even_stock, name='update_even_stock'),
]