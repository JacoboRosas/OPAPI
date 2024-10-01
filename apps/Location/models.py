from django.db import models
from apps.Sea.models import Sea 
# Create your models here.

class Location(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    name = models.CharField(max_length=50, blank=False, null=False)
    sea_id = models.ForeignKey(Sea, on_delete=models.CASCADE)

    # ------- We define here how the data entry will be shown ------- #    
    def __str__(self):
        return self.name

