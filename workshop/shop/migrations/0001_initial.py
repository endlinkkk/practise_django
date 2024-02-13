# Generated by Django 5.0.2 on 2024-02-10 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('home_address', models.TextField(verbose_name='Домашний адрес')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время приема заказа')),
                ('work_type', models.TextField(verbose_name='Тип выполняемой работы')),
                ('tariff', models.CharField(choices=[('classic', 'Обычный'), ('express', 'Экспресс')], default='classic', max_length=100, verbose_name='Тариф')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to='shop.client')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_orders', to='shop.master')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-order_date_time'],
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_time', models.DateTimeField(verbose_name='Дата и время начала работы')),
                ('close_date_time', models.DateTimeField(verbose_name='Дата и время закрытия ордера')),
                ('volume', models.TextField(verbose_name='Объем выполненной работы')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
            options={
                'verbose_name': 'Детали заказа',
                'verbose_name_plural': 'Детали заказов',
                'ordering': ['-start_date_time'],
            },
        ),
    ]
