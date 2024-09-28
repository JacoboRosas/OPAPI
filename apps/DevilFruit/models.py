from django.db import models

# Create your models here.

class DevilFruit(models.Model):
    df_name = models.CharField(max_length=20)
    df_jp_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    current_owner = models.BooleanField(default=True)
    awakened = models.BooleanField()

    def __str__(self):
        return self.df_name
