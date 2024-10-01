from django.db import models
# We import the character model, so we can get its foreign key
from apps.Character.models import Character

# Create your models here.

class Bounty(models.Model):
    # ------- We import any attributes here (primary keys are created by default) ------- #
    # Added the character table foreign key. By default, when adding anything through the CRUD, it will show all the characters available.
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    bounty_amount = models.BigIntegerField(blank=False, null=False)
    
    # ------- We define here how the data entry will be shown ------- #
    def __str__(self):
        # Since we are returning a integer value, we need to convert it to string, since __str___ means string.
        # For this, we can just do f"{}", this embeds any expression inside the curly braces within a string.
        # So basically, anything inside this will be a string when displayed, but the actual value will still be
        # the integer.
        return f"{self.bounty_amount}"
