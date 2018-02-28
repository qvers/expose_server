from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)


class Exposition(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название выставки')
    description = models.CharField(max_length=200, verbose_name='Описание выставки', null=True)
    expiration_date = models.DateTimeField('дата окончания', null=True, blank=True)


class Picture(models.Model):
    exposition = models.ForeignKey(Exposition, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures')