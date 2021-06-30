from django.db import models

# Create your models here.

class Credit(models.Model):
    fullname = models.CharField(max_length=200)
    monto = models.IntegerField()
    sentinel = models.CharField(max_length=200)
    ai = models.IntegerField()
    
    