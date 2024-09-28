from django.db import models

# Create your models here.

class Faction(models.Model):
    rank = models.CharField(max_length=20)
    faction_name=models.CharField(max_lenght=20)
    # We can do this instead

    # current_faction = models.BooleanField()

    #By doing this, the default will be False
    current_faction = models.BooleanField(default=True)

    def __str__(self):
        return self.faction_name
