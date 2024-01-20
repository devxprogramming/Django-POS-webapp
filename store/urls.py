from django.urls import path
from . import views

from .views import CreatProduct, ProductList, ProductDetail, CreateSale, SaleList, SaleDetail


urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('add-product/', CreatProduct.as_view(), name='add_product'),
    path('add-sale/', CreateSale.as_view(), name='add_sale'),
    path('all-products/', ProductList.as_view(), name='all_products'),
    path('all-sales/', SaleList.as_view(), name='all_sales'),
    path('product-detail/<pk>', ProductDetail.as_view(), name='product_detail'),
    path('sale-detail/<pk>', SaleDetail.as_view(), name='sale_detail'),
]
