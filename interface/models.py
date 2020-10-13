from django.db import models

class s2_1(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=20)
    capacity            = models.IntegerField(default=30)
    occupied            = models.IntegerField(default=0)

class s2_b1(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=20)
    capacity            = models.IntegerField(default=30)
    occupied            = models.IntegerField(default=0)

class s2_b2(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=20)
    capacity            = models.IntegerField(default=30)
    occupied            = models.IntegerField(default=0)

class s2_b3(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=20)
    capacity            = models.IntegerField(default=30)
    occupied            = models.IntegerField(default=0)

class s2_b4(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=20)
    capacity            = models.IntegerField(default=30)
    occupied            = models.IntegerField(default=0)