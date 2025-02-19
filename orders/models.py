from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('en attente', 'En attente'),
        ('en cours', 'En cours'),
        ('livrée', 'Livrée'),
        ('annulée', 'Annulée'),
    )

    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="commandes")
    adresse_livraison = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en attente')
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande {self.id} - {self.client.username}"

    @property
    def total_price(self):
        total = 0
        for order_product in self.orderproduct_set.all():
            total += order_product.product.price * order_product.quantity
        return total


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
