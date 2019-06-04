from django.db import models

class Product(models.Model):
    name = models.TextField(default='')
    quantity = models.TextField(default='')
    pieces = models.IntegerField(default=1)
