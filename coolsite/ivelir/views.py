from django.http import HttpResponse, HttpResponseNotFound ,HttpResponseServerError, HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotModified
from django.shortcuts import render, redirect,reverse

from .forms import PurchaseForm
from django.contrib.auth.models import User
from .models import Customer, Supplier, Review, Jewelry, User


def jewelry_list(request):
    jewelries = Jewelry.objects.all()
    return render(request, 'jewelry_list.html', {'jewelries': jewelries},)

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})
def oformlenie(request):
    return render(request, 'oformlenie.html')


def purchase_page(request):
    form = PurchaseForm()

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            user = User(name=name, email=email)
            user.save()

            return redirect('purchase_page')

    users = User.objects.all()
    return render(request, 'purchase_page.html', {'form': form, 'users': users})
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def index(request):
    data = {
        'title': 'Главная страница',
        'values':['some','hello','123']
    }
    return render(request,'index.html',data)
def masters(request,masterid):
    return HttpResponse(f"<h1> Мастер номер </h1><p>{masterid}<p>")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
#500
def server_error_handler(request):
    return HttpResponseServerError('<h1>Внутренняя ошибка сервера</h1>')

#403
def forbidden_error_handler(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещен</h1>')

#303
def not_modified_error_handler(request, exception):
    return HttpResponseNotModified('<h1>Ресурс не модифицирован</h1>')

#302
def redirect_error_handler(request, exception):
    return HttpResponseRedirect('<h1>Перенаправляю на ссылку</h1>')

