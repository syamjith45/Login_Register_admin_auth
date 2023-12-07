# models.py

from django.db import models

class Product(models.Model):
    """
    Model representing a product in your application.
    """

    # Product Name
    name = models.CharField(max_length=255, help_text="Enter the product name")

    # Product Category
    category = models.CharField(max_length=50, choices=[
        ('sports', 'Sports Equipment'),
        ('clothing', 'Sportswear'),
        # Add more categories as needed
    ], help_text="Select the product category")

    # Product Price
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the product price")

    # Product Stock
    stock = models.PositiveIntegerField(help_text="Enter the product stock")
    
    #product image
    image = models.ImageField(upload_to='media/', null=True, blank=True, help_text="Upload product image")


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
