from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('master/<int:masterid>/', views.masters, name='masters'),
    path('customers/', views.customer_list, name='customer_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('jewelries/', views.jewelry_list, name='jewelry_list'),
    path('oformlenie/', views.oformlenie, name='oformlenie'),
    path('purchase_page/', views.purchase_page, name='purchase_page'),

]