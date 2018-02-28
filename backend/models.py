from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)


class Exposition(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=200, verbose_name='Название выставки')


class Picture(models.Model):
    exposition = models.ForeignKey(Exposition, null=True)
    image = models.ImageField(upload_to='pictures')