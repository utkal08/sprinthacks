from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    CHOICES=(('M','Manufacturer'),('R','Retailer'))
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    USERNAME_FIELD='user.username'
    name=models.CharField(max_length=50,default='NaN')
    phone=models.BigIntegerField(null=True)
    address=models.TextField()
    user_type=models.CharField(max_length=15,choices=CHOICES)
    image=models.ImageField(upload_to="static/user_images",default= "static/images/cart.png")

    def __str__(self):
        return self.name


    def save(self,force_insert=False):
        super().save(force_insert)
        img=Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    