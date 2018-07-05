from django.db import models
import json
import os

class Serie(models.Model):
    title = models.CharField(max_length = 200)
    resume = models.TextField()
    link = models.TextField()
    rate = models.TextField()
    genre = models.TextField()
    cast = models.TextField()


  

    
