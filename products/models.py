from django.db import models

class Stock(models.Model):
    """
    Represents the stock information of a product.
    """
    quantity = models.IntegerField()

    def __str__(self):
        return f"Stock: {self.quantity}"


class Product(models.Model):
    """
    Represents a product in the shop.
    """
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    product_description = models.TextField()
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name