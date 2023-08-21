from django.db import models
from users.models import User

class ProductsCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='poducts_image')
    category = models.ForeignKey(to=ProductsCategory, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE )
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE )
    quantity = models.PositiveSmallIntegerField(default=0)
    craated_timestamp = models.DateTimeField(auto_now_add=True)
    
    def sum(self):
        return self.product.price * self.quantity