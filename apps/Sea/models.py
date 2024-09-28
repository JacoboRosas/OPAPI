from django.db import models

# Create your models here.

class Sea(models.Model):
    name = models.CharField(max_length=15, blank=False , null=False)
      
    def __str__(self):
        return self.name
