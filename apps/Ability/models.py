from django.db import models

# Create your models here.

class Ability(models.Model):
    ability_name = models.CharField(max_lenght=40)
    ability_type = models.CharField(max_lenght=20)
    description = models.CharField(max_lenght=20)
    
    def __str__(self):
        return self.ability_name
