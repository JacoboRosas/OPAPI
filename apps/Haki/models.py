from django.db import models

# Create your models here.


class Haki(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    JPname = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return self.name
    

