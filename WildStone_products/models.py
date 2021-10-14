from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.db.models.deletion import CASCADE

class customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=CASCADE)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.firstname

class Category(models.Model):
    name=models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name



# Create your models here.
class Product(models.Model):
    type=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,blank=True)
    price=models.CharField(max_length=255,default='')
    Image_url=models.CharField( max_length=2085,default='',blank=True)
    Description=models.CharField(max_length=255,default='')
    def __str__(self):
        return self.name

class Status(models.Model):
    status=models.CharField( max_length=255,default='')
    type=models.CharField(null=True, max_length=255,default='')
    def __str__(self):
        return self.status



class Order(models.Model):
    customer_name=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    # Get_on=models.DateField()
    def __str__(self):
        return self.product.name
# Create your models here.

class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    images = models.ImageField(null=False,blank=False)
    desc = models.CharField(max_length=255, null=False,blank=False)
    def __str__(self):
        return self.category.name
