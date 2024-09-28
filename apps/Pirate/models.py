from django.db import models
from apps.Faction.models import Faction

# Create your models here.
class Pirate(models.Model):
    #Django doesn't need to define primary keys, it does it automatically
    #so we don't need to add crew_id as another attribute
    
    #If we wish however, we can add the below command to create a custom ID
    #that acts like a primary key

    #crew_id = models.CharField(max_lenght=100, primary_key=true)

    #Another note, we don't need to add the _id at the end of the foreign key
    #this is because django already does it by itself, and creates a column like <field_name>_id
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    crew_name = models.CharField(max_length=40)
    ship_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.crew_name} of the {self.ship_name}"