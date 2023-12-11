from django.urls import path
from django.urls import path
from .views import index, masters, customer_list, supplier_list, review_list, jewelry_list

urlpatterns = [
    path('', index, name='index'),
    path('master/<int:masterid>/', masters, name='masters'),
    path('customers/', customer_list, name='customer_list'),
    path('suppliers/', supplier_list, name='supplier_list'),
    path('reviews/', review_list, name='review_list'),
    path('jewelries/', jewelry_list, name='jewelry_list'),

]