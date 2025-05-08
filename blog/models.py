from django.db import models

class Post(models.Model):
    titile = models.CharField(max_length=100)
