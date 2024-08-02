from django.db import models


class Aohan(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)