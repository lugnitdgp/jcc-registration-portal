from __future__ import unicode_literals
from django.shortcuts import render
from .models import Team
from .forms import RegistrationForm


def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_team = Team(
                team_name = request.POST['team_name'] ,
                player_one_name = request.POST['player_one_name'],
                player_two_name = request.POST['player_two_name']
            )
            new_team.save()
            return render(request , 'success.html')
    else:
        form = RegistrationForm()

    context = { 'form' : form }
    return render(request , 'register.html' , context)

