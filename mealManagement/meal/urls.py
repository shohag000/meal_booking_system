from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/',views.get_login,name='login'),
    path('logout/',views.get_logout,name='logout'),
    path('chart/',views.chart,name='meal_sheet'),
    path('shopping_date/',views.shopping_date,name='shopping_date'),
    path('order_meal/<date>/', views.order, name='order'),
    #re_path(r'^order_meal/(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/$', views.order, name='order'),


]
