from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    CHOICES=(('M','Manufacturer'),('R','Retailer'))
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    USERNAME_FIELD='user.username'
    username=models.CharField(max_length=50,default='NaN')
    phone=models.BigIntegerField()
    address=models.TextField()
    user_type=models.CharField(max_length=15,choices=CHOICES)
    image=models.ImageField(upload_to="static/user_images")

    def __str__(self):
        return self.name


    def save(self,force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        img=Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    