from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import uuid


class Team(models.Model):
    team_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    player_one_name = models.CharField(
        max_length=255, default="No Player Assigned")
    player_one_email = models.EmailField(
        max_length=255, default="No Email Provided")
    player_one_contact = models.BigIntegerField(blank=True, null=True)
    player_one_hall = models.IntegerField(blank=True, null=True)
    player_two_name = models.CharField(
        max_length=255, default="No Player Assigned")
    player_two_email = models.EmailField(
        max_length=255, default="No Email Provided")
    player_two_contact = models.BigIntegerField(blank=True, null=True)
    player_two_hall = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.team_name)
