from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=127)
    surname = models.CharField(max_length=127)

    def __str__(self):
        return f'{self.name} {self.surname}'
    