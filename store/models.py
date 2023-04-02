from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    #manufacturer=models.ManyToManyField()
    price=models.IntegerField()
    image=models.ImageField()

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()

    def __str__(self):
        return self.name
    