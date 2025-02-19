from itertools import product
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import *
from .forms import ProductForm 



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a page that shows all products
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# View for listing orders
def order_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    orders = Order.objects.all()

    if search_query:
        orders = orders.filter(client__username__icontains=search_query)

    if status_filter:
        orders = orders.filter(statut=status_filter)

    return render(request, 'orders.html', {'orders': orders, 'search_query': search_query, 'status_filter': status_filter})

# View to create a new order
@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user  # Assign the logged-in user as the client
            order.save()

            # Check and log selected products
            print("Selected products:", form.cleaned_data['products'])

            # Link selected products to the order
            for product in form.cleaned_data['products']:
                OrderProduct.objects.create(order=order, product=product, quantity=1)

            return redirect('order_confirmation', order_id=order.id)  # Redirect to the confirmation page
        else:
            print("Form is not valid. Errors: ", form.errors)  # Debugging line
    else:
        form = OrderForm()

    products = Product.objects.all()  # Fetch all products to display in the dropdown
    return render(request, 'create_order.html', {'form': form, 'products': products})

    return render(request, 'create_order.html', {'form': form, 'products': products})



# View to confirm the order (update order status to "en cours")
@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.client == request.user:  # Ensure only the order owner can confirm
        if request.method == 'POST':
            order.statut = 'en cours'  # Change status to "in progress"
            order.save()
            return redirect('order_list')  # Redirect to the order list after confirmation

    return render(request, 'order_confirmation.html', {'order': order})

