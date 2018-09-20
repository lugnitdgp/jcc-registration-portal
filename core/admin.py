from __future__ import unicode_literals

from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):

    list_display = (
        u'team_id',
        'team_name',
        'player_one_name',
        'player_two_name'
    )

admin.site.register(Team , TeamAdmin)

