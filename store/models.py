from django.db import models
from PIL import Image

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    #manufacturer=models.ManyToManyField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='static/product_images')

    def __str__(self):
        return self.name
    
    def save(self,force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        img=Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Manufacturer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()

    def __str__(self):
        return self.name
    