from django.db import models

# Create your models here.

class DevilFruit(models.Model):
    df_name = models.CharField(max_length=20)
    df_jp_name = models.CharField(max_lenght=20)
    category = models.CharField(max_lenght=20)

    def __str__(self):
        return self.df_name
