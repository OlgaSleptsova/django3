from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    x = request.GET.get('sort')
    template = 'catalog.html'
    if x =='name':
        phone = Phone.objects.all().values()
        sort_phone = sorted(phone, key=lambda p: p['name'])
        context = {'phones': sort_phone}
    elif x == 'min_price':
        phone = Phone.objects.all().values()
        sort_phone = sorted(phone, key=lambda p: p['price'])
        context = {'phones': sort_phone}
    elif x == 'max_price':
        phone = Phone.objects.all().values()
        sort_phone = sorted(phone, key=lambda p: p['price'],reverse=True)
        context = {'phones': sort_phone}
    elif x == None:

        context = {'phones': Phone.objects.all()}
    return render(request, template, context)



def show_product(request, slug):
    template = 'product.html'

    phone = phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone':phone}
    return render(request, template, context)



