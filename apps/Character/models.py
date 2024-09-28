from django.db import models
from apps.Arc.models import Arc
from apps.Ability.models import Ability
from apps.Bounty.models import Bounty
from apps.DevilFruit.models import DevilFruit
from apps.Faction.models import Faction
from apps.Haki.models import Haki
from apps.Location.models import Location
# Create your models here.


CHOICES = (
    ('Human'),
    ('Fishmen'),
)

class Character(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=10, choices=('Alive', 'Dead', 'Unknown'), blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    race = models.CharField(max_length=30, choices=CHOICES, null=False, blank=False, default='Human')
    birthday = models.DateField()
    height = models.DecimalField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    abilitys = models.ManyToManyField(Ability)
    arcs = models.ManyToManyField(Arc)
    bountys = models.ManyToManyField(Bounty)
    devil_fruits = models.ManyToManyField(DevilFruit)
    factions = models.ManyToManyField(Faction)
    hakis = models.ManyToManyField(Haki)
    
def __str__(self):
    return self.name

    