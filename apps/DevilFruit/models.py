from django.db import models

# Create your models here.

class DevilFruit(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    df_name = models.CharField(max_length=50)
    df_jp_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    #current_owner = models.BooleanField(default=True)
    #awakened = models.BooleanField()

    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        return self.df_name
