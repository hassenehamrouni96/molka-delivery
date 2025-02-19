from django.urls import path
from .views import add_product, order_list, product_list
from orders import views

urlpatterns = [
     path('products/', product_list, name='product_list'),
     path('add-product/', add_product, name='add_product'),
     path('commandes/', order_list, name='order_list'),
     path('create-order/', views.create_order, name='create_order'),
      path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
