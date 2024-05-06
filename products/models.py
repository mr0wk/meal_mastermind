from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    num_of_kcal = models.IntegerField()

    def __str__(self):
        return self.name
