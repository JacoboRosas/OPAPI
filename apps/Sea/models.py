from django.db import models

# Create your models here.

class Sea(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    name = models.CharField(max_length=15, blank=False , null=False)

     # ------- We define here how the data entry will be shown ------- #     
    def __str__(self):
        return self.name
