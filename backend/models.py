from django.db import models

class Exposition(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название выставки')

