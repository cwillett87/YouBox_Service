from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Role(models.Model):
    type = models.CharField(primary_key=True, max_length=50)


class User(AbstractUser):
    role = models.ForeignKey('subscribers.Role', null=True, on_delete=models.CASCADE)
    image_Id = models.ForeignKey('subscribers.Image', null=True, on_delete=models.CASCADE)
    street_Address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_Code = models.CharField(max_length=100)
    phone = models.BigIntegerField(blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'role', 'street_Address', 'city', 'state', 'zip_Code', 'phone']


class Utoken(models.Model):
    user_Id = models.ForeignKey('subscribers.User', null=True, on_delete=models.CASCADE)


class Clothing(models.Model):
    image_Id = models.ForeignKey('subscribers.Image', null=True, on_delete=models.CASCADE)
    user_Id = models.ForeignKey('subscribers.User', null=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


#setup static folder and image directory to store images
class Image(models.Model):
    user_Id = models.ForeignKey('subscribers.User', null=True, on_delete=models.CASCADE)
    item_Id = models.ForeignKey('subscribers.Clothing', null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True)


class Subscription(models.Model):
    user_Id = models.ForeignKey('subscribers.User', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number_Items = models.IntegerField(null=True)
    price = models.DecimalField(default=0, max_digits=60, decimal_places=2)
    delivery_Freq = models.CharField(max_length=100)


class Order(models.Model):
    user_Id = models.ForeignKey('subscribers.User', null=True, on_delete=models.CASCADE)
    subscription_Id = models.ForeignKey('subscribers.Subscription', null=True, on_delete=models.CASCADE)
    clothing_Items = models.ManyToManyField(Clothing, null=True)
    total = models.DecimalField(default=0, max_digits=60, decimal_places=2)
    est_Delivery = models.DateField(null=True, blank=True)


