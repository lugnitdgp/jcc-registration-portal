from __future__ import unicode_literals

from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):

    list_display = (
        'team_name',
        'player_one_name',
        'player_one_email',
        'player_one_hall',
        'player_two_name',
        'player_two_email',
        'player_two_hall'
    )


admin.site.register(Team, TeamAdmin)
