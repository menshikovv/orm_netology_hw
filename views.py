from django.shortcuts import render
from .models import Phone

def catalog(request):
    sort_param = request.GET.get('sort', 'name')
    phones = Phone.objects.all()

    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    return render(request, 'catalog.html', context)

def phone_detail(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, 'phone_detail.html', context)
