from django.urls import path
from .views import main_view, add_master, add_client, add_order, add_order_detail

urlpatterns = [
    path('', main_view, name='home'),
    path('add_master', add_master, name='add_master'),
    path('add_client', add_client, name='add_client'),
    path('add_order', add_order, name='add_order'),
    path('add_order_detail', add_order_detail, name='add_order_detail'),
]
