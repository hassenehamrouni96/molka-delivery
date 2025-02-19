from django import forms
from .models import Order, OrderProduct, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['adresse_livraison']

    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )


    def save(self, commit=True):
        # Save the order instance
        order = super().save(commit=False)
        if commit:
            order.save()

        # Create the order-product relationship
        for product in self.cleaned_data['products']:
            OrderProduct.objects.create(order=order, product=product, quantity=1)  # Default quantity is 1

        return order
