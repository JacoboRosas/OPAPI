from django.db import models
from apps.Arc.models import Arc
from apps.Ability.models import Ability
# Removed bounty import, this was not intended. If I left any import here related to bounty, while I was importing the character to the bounty
# app, there would be an error basically making a loop with importation as the main issue. So just take that into account.
from apps.DevilFruit.models import DevilFruit
from apps.Faction.models import Faction
from apps.Haki.models import Haki
from apps.Location.models import Location
from apps.Pirate.models import Pirate
from apps.Marine.models import Marine
# Create your models here.


CHOICESRACE= (
    ('human', "Human"),
    ('fishmen', 'Fishman'),
)

CHOICESTATUS = (
    ('alive' , 'Alive' ),
    ('dead ' , 'Dead' ),
    ('unknwon' , 'Unknown'),
)
class Character(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=10, choices=CHOICESTATUS, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    race = models.CharField(max_length=30, choices=CHOICESRACE, null=False, blank=False, default='Human')
    birthday = models.DateField()
    height = models.DecimalField(decimal_places=2, max_digits=4)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    
    # ------- We import any MANY TO MANY relationship here ------- #
    # Removed bounty many to many relationship. This was not intended.
    arc = models.ManyToManyField(Arc)
    ability = models.ManyToManyField(Ability)
    devil_fruit = models.ManyToManyField(DevilFruit)
    faction = models.ManyToManyField(Faction)
    haki = models.ManyToManyField(Haki)
    pirate = models.ManyToManyField(Pirate, blank=True)
    marine = models.ManyToManyField(Marine, blank=True)

    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.name

    