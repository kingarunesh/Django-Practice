from django.db import models


class Aohan(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()