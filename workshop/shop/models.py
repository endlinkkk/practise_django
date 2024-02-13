from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    birth_date = models.DateField(verbose_name='Дата рождения')
    home_address = models.TextField(verbose_name='Домашний адрес')
    phone_number = models.CharField(max_length=11, verbose_name='Телефон')

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f"{self.full_name}"


class Master(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self) -> str:
        return f"{self.full_name}"


class Order(models.Model):
    TARIFF_OPTIONS = (
        ('classic', 'Обычный'),
        ('express', 'Экспресс'),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_orders')
    order_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время приема заказа')
    work_type = models.TextField(verbose_name='Тип выполняемой работы')
    tariff = models.CharField(choices=TARIFF_OPTIONS, default='classic', verbose_name='Тариф', max_length=100)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='master_orders')

    class Meta:
        ordering = ['-order_date_time']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderDetail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(verbose_name='Дата и время начала работы')
    close_date_time = models.DateTimeField(verbose_name='Дата и время закрытия ордера')
    volume = models.TextField(verbose_name='Объем выполненной работы')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')

    class Meta:
        ordering = ['-start_date_time']
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'
