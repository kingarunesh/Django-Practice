from django.db import models


class First(models.Model):
    title = models.CharField(max_length=250)