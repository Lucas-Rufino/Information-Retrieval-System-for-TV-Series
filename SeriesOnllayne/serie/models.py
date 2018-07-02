from django.db import models
import json
import os

class Serie(models.Model):
    title = models.CharField(max_length = 200)
    resume = models.TextField()
    link = models.TextField()
    rate = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    
    def get_data(self,id):
        path = "data"
        filename = id
        fullpath = os.path.join(path, filename)
        with open(fullpath) as json_data:
            d = json.load(json_data)
            return d

    def make_serie(self, id):
        data = self.get_data(id)
        self.title = data['title']
        self.resume = data['resume']
        self.rate = data['rate']
        self.link = data['link']
    
