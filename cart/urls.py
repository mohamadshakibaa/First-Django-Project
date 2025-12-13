from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/', views.add, name='views.add'),
    path('delete/', views.delete, name='views.delete'),
    path('update/', views.update, name='views.update'),
]