from django.db import models

# Create your models here.

class Arc(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    arc_name = models.CharField(max_length=40)
    arc_lenght = models.IntegerField()
    
    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.arc_name
