from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Customer, Supplier, Review,Jewelry
def jewelry_list(request):
    jewelries = Jewelry.objects.all()
    return render(request, 'jewelry_list.html', {'jewelries': jewelries})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def index(request):
    return render(request,'index.html')
def masters(request,masterid):
    return HttpResponse(f"<h1> Мастер номер </h1><p>{masterid}<p>")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

