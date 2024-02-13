from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from .forms import ClientForm, MasterForm, OrderForm, OrderDetailForm
from .utils import is_administrators_group, is_master_group, is_administrator_or_master
from .models import Client, Master, Order, OrderDetail



def administrator(request):
    masters = Master.objects.all()
    client = Client.objects.all()
    order = Order.objects.all()
    order_detail = OrderDetail.objects.all()
    print(client)
    data = {
        'masters': masters,
        'clients': client,
        'orders': order,
        'order_details': order_detail,
    }
    return render(request=request, template_name='shop/administrator.html', context=data)


def master(request):
    order = Order.objects.all()
    order_detail = OrderDetail.objects.all()
    data = {
        'orders': order,
        'order_details': order_detail,
    }
    return render(request=request, template_name='shop/master.html', context=data)



def main_view(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)

    else:
        if is_administrators_group(request.user):
            return administrator(request)
        elif is_master_group(request.user):
            return master(request)
        else:
            logout_url = reverse('logout')
            return redirect(logout_url)


@login_required
@user_passes_test(is_administrators_group)
def add_client(request):
    """Представление для добавления клиента"""
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            print('форма валидна')
            full_name = form.data['full_name']
            birth_date = form.data['birth_date']
            home_address = form.data['home_address']
            phone_number = form.data['phone_number']
            client = Client.objects.create(full_name=full_name, birth_date=birth_date, home_address=home_address, phone_number=phone_number)
            client.save()
        return HttpResponseRedirect('/')
    else:
        form = ClientForm()
    return render(request=request, template_name='shop/add_client.html', context={'form': form})



@login_required
@user_passes_test(is_administrators_group)
def add_master(request):
    """Представление для добавления мастера"""
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            full_name = form.data['full_name']
            master = Master.objects.create(full_name=full_name)
            master.save()
        return HttpResponseRedirect('/')
    else:
        form = MasterForm()
    return render(request=request, template_name='shop/add_master.html', context={'form': form})


@login_required
@user_passes_test(is_administrator_or_master)
def add_order(request):
    """Представление для добавления заказа"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print(form.data)
            client = form.cleaned_data['client']
            order_date_time = form.data['order_date_time_0'] + ' ' + form.data['order_date_time_1']
            work_type = form.data['work_type']
            tariff = form.data['tariff']
            master = form.cleaned_data['master']
            order = Order.objects.create(client=client, order_date_time=order_date_time, work_type=work_type, tariff=tariff, master=master)
            order.save()
            order_id = order.id
            request.session['order_id'] = order_id
            return HttpResponseRedirect('/add_order_detail')
    else:
        form = OrderForm()
    return render(request=request, template_name='shop/add_order.html', context={'form': form})


@login_required
@user_passes_test(is_administrator_or_master)
def add_order_detail(request):
    """Представление для добавления деталей заказа"""
    order_id = request.session['order_id']
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = OrderDetailForm(request.POST, order=order)
        if form.is_valid():
            start_date_time = form.data['start_date_time_0'] + ' ' + form.data['start_date_time_1']
            close_date_time = form.data['close_date_time_0'] + ' ' + form.data['close_date_time_1']
            volume = form.data['volume']
            price = form.data['price']
            order_detail = OrderDetail(order=order, start_date_time=start_date_time, close_date_time=close_date_time, volume=volume, price=price)
            order_detail.save()
            return HttpResponseRedirect('/')
    else:
        form = OrderDetailForm(order=order)

    return render(request=request, template_name='shop/add_order_detail.html', context={'form': form})