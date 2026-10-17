from django.db import models


class ProductModel(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    price=models.PositiveIntegerField(null=True)
    quantity=models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.product_name}'