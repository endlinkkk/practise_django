from django import forms
from .widgets import MinimalSplitDateTimeMultiWidget


from .models import Client, Master, Order

class ClientForm(forms.Form):
    full_name = forms.CharField(max_length=200, label='ФИО', required=True)
    birth_date = forms.DateField(label='Дата рождения', required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    home_address = forms.CharField(widget=forms.Textarea, label='Домашний адрес', required=True)
    phone_number = forms.CharField(max_length=11, label='Телефон', required=True)


class MasterForm(forms.Form):
    full_name = forms.CharField(max_length=200, label='ФИО', required=True)


class OrderForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Клиент', required=True)
    order_date_time = forms.DateTimeField(label='Дата и время приема заказа', required=True, widget=MinimalSplitDateTimeMultiWidget())
    work_type = forms.CharField(widget=forms.Textarea, label='Тип выполняемой работы', required=True)
    tariff = forms.ChoiceField(choices=Order.TARIFF_OPTIONS, label='Тариф', required=True)
    master = forms.ModelChoiceField(queryset=Master.objects.all(), label='Мастер', required=True)


class OrderDetailForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self.order = kwargs.pop('order')
        super(OrderDetailForm, self).__init__(*args, **kwargs)

    start_date_time = forms.DateTimeField(label='Дата и время начала работы', required=True, widget=MinimalSplitDateTimeMultiWidget())
    close_date_time = forms.DateTimeField(label='Дата и время закрытия ордера', widget=MinimalSplitDateTimeMultiWidget())
    volume = forms.CharField(widget=forms.Textarea, label='Объем выполненной работы', required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Стоимость', required=True)
    