from django.db import models

# Create your models here.

class Faction(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- # 
    # Delete "rank" attribute, it shouldn't be here, but rather, in the child tables.
    faction_name=models.CharField(max_length=20)
    # We can do this instead

    # current_faction = models.BooleanField()

    #By doing this, the default will be False
    current_faction = models.BooleanField(default=True)

    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.faction_name
