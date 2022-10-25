from django.db import models


# Create your models here.


class Persons(models.Model):
    name = models.CharField(max_length=100)
    pasn = models.CharField(max_length=100, default=0000)


class reg(models.Model):
    name = models.CharField(max_length=100)
    pasn1 = models.CharField(max_length=100, default=0000)
    pasn2 = models.CharField(max_length=100, default=0000)
    email = models.EmailField(max_length=254)


class admins(models.Model):
    adminname = models.CharField(max_length=100)
    roomnum = models.CharField(max_length=100)
    reso = models.TextField()
