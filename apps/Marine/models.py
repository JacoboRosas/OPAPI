from django.db import models
from apps.Faction.models import Faction

# Create your models here.
class Marine(models.Model):
    #Django doesn't need to define primary keys, it does it automatically
    #so we don't need to add crew_id as another attribute
    
    #If we wish however, we can add the below command to create a custom ID
    #that acts like a primary key

    #marine_id = models.CharField(max_lenght=100, primary_key=true)

    #Another note, we don't need to add the _id at the end of the foreign key
    #this is because django already does it by itself, and creates a column like <field_name>_id
    
    # ------- We import any attributes here (primary keys are created by default) ------- #
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    rank = models.CharField(max_length=20)

    # Se hace esto para que no retorne ppr default el nombre object, sino para que retorne el nombre del modelo + el contenido del atributo al que hace referencia
    # en este caso, rank
    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.rank