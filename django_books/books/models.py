from django.db import models

# Create your models here.
# book is subclass of django.db.models.Model
# pk (id) get automatically added during migraiton

class Book(models.Model):
    rank = models.IntegerField()
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    year = models.IntegerField()
    
    def __str__(self):
        return self.author
