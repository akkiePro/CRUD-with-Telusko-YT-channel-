from django.db import models


# Create your models here.
class Destination(models.Model):
    #id: int
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)     # description
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
