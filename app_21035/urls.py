from django.contrib import admin
from django.urls import path
from .views import ProductExportCSVView
from . import views

urlpatterns = [
    path('', views.home),
    path('productfamily/', views.ProductFamilyList.as_view(), name='productfamily_list'),
    path('productfamily/add', views.ProductFamilyCreate.as_view(), name='productfamily_create'),
    path('productfamily/<int:pk>/', views.ProductFamilyDetail.as_view(), name='productfamily_detail'),
    path('productfamily/update/<int:pk>/', views.ProductFamilyUpdate.as_view(), name='productfamily_update'),
    path('productfamily/delete/<int:pk>/', views.ProductFamilyDelete.as_view(), name='productfamily_delete'),
    
    path('product/', views.ProductList.as_view(), name='product_list'),
    path('product/add', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),

    path('sellingpoint/', views.SellingPointList.as_view(), name='sellingpoint_list'),
    path('sellingpoint/add', views.SellingPointCreate.as_view(), name='sellingpoint_create'),
    path('sellingpoint/<int:pk>/', views.SellingPointDetail.as_view(), name='sellingpoint_detail'),
    path('sellingpoint/update/<int:pk>/', views.SellingPointUpdate.as_view(), name='sellingpoint_update'),
    path('sellingpoint/delete/<int:pk>/', views.SellingPointDelete.as_view(), name='sellingpoint_delete'),

    path('price/', views.PriceList.as_view(), name='price_list'),
    path('price/add', views.PriceCreate.as_view(), name='price_create'),
    path('price/<int:pk>/', views.PriceDetail.as_view(), name='price_detail'),
    path('price/update/<int:pk>/', views.PriceUpdate.as_view(), name='price_update'),
    path('price/delete/<int:pk>/', views.PriceDelete.as_view(), name='price_delete'),

    path('basket/', views.BasketList.as_view(), name='basket_list'),
    path('basket/add', views.BasketCreate.as_view(), name='basket_create'),
    path('basket/<int:pk>/', views.BasketDetail.as_view(), name='basket_detail'),
    path('basket/update/<int:pk>/', views.BasketUpdate.as_view(), name='basket_update'),
    path('basket/delete/<int:pk>/', views.BasketDelete.as_view(), name='basket_delete'),

    path('productbasket/', views.ProductBasketList.as_view(), name='productbasket_list'),
    path('productbasket/add', views.ProductBasketCreate.as_view(), name='productbasket_create'),
    path('productbasket/<int:pk>/', views.ProductBasketDetail.as_view(), name='productbasket_detail'),
    path('productbasket/update/<int:pk>/', views.ProductBasketUpdate.as_view(), name='productbasket_update'),
    path('productbasket/delete/<int:pk>/', views.ProductBasketDelete.as_view(), name='productbasket_delete'),

    path('export/products/', ProductExportCSVView.as_view(), name='export_products_csv'),

    path('import/product',views.import_product, name='data-product'),

    path('export/product-family/', views.export_product_family, name='export-product-family'),

    path('product_family_import/',views.import_product_family, name='import-product-family'),

    path('import/selling-point/', views.import_selling_point, name='import-selling-point'),

    path('export/selling-point/', views.SellingPointExportCSVView.as_view(), name='export-selling-point'),
    path('export/price/', views.PriceExportCSVView.as_view(), name='export-price'),
    path('import/price/', views.import_price, name='import-price'),
    path('export/basket/', views.BasketExportCSVView.as_view(), name='export-basket'),
    path('import/basket/', views.import_basket, name='import-basket'),
    path('export/product_basket/', views.BasketExportCSVView.as_view(), name='export-product-basket'),
    path('import/product_basket/', views.import_basket, name='import-product-basket'),
    
]
