from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import uuid


class Team(models.Model):
    team_id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    team_name = models.CharField(max_length=255)
    player_one_name = models.CharField(max_length=255,default="No Player Assigned")
    player_two_name = models.CharField(max_length=255,default="No Player Assigned")
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.team_name)



