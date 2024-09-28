from django.db import models

# Create your models here.

class Arc(models.Model):
    arc_name = models.CharField(max_lenght=40)
    arc_lenght = models.IntegerField()
    
    def __str__(self):
        return self.arc_name
