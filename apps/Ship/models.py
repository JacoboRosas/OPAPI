from django.db import models

# Create your models here.
class Ship(models.Model):
    #Django doesn't need to define primary keys, it does it automatically
    #so we don't need to add crew_id as another attribute
    
    #If we wish however, we can add the below command to create a custom ID
    #that acts like a primary key
    
    # ------- We import any attributes here (primary keys are created by default) ------- #
    ship_name = models.CharField(max_length=40)

    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.ship_name