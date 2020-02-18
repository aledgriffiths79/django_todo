from django.db import models

# Create your models here. Item will be a model that was created in a models.py file. Models is the structure of a database entry i.e name, done.
class Item(models.Model):
  name = models.CharField(max_length=30, blank=False)
  done = models.BooleanField(blank=False, default=False)

  def __str__(self):
    return self.name
