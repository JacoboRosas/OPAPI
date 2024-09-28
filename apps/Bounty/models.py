from django.db import models

# Create your models here.

class Bounty(models.Model):
    char_id = models.IntegerField(blank=False, null=False)
    bounty_amount = models.BigIntegerField(blank=False, null=False)
    
    def __str__(self):
        return self.bounty_amount
