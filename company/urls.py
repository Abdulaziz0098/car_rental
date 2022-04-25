from django.contrib import admin
from django.urls import path, include

from company import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('brand/', views.brand_page, name='brand'),
    path('contact/', views.contact_page, name='contact'),
    path('fine/', views.fine_page, name='fine'),
    path('listing/', views.listing_page, name='listing'),
    path('payment/<int:pk>/', views.payment_page, name='payment'),
    path('supply/', views.supply_page, name='supply'),
]
