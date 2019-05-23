from django.db import models

class Product(models.Model):
    name = models.TextField(default='')

    def __str__(self):
        return self.name
