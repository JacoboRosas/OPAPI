from django.db import models

# Create your models here.

class Ability(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    ability_name = models.CharField(max_length=40)
    ability_type = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    
    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.ability_name
