from __future__ import unicode_literals
from django.shortcuts import render
from .models import Team
from .forms import RegistrationForm
from . import service


def index(request):

    is_team_name_taken = False

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            team_name = request.POST['team_name']
            player_one_contact = request.POST['player_one_contact']
            player_two_contact = request.POST['player_two_contact']
            player_one_email = request.POST['player_one_email']
            player_two_email = request.POST['player_two_email']

            team = Team.objects.filter(
                player_one_email=player_one_email, player_two_email=player_two_email).first()

            if not team:
                unique_team_id = service.generate(
                    team_name + player_one_contact + player_two_contact)
                new_team = Team(
                    team_name=request.POST['team_name'],
                    player_one_name=request.POST['player_one_name'],
                    player_one_email=request.POST['player_one_email'],
                    player_one_contact=request.POST['player_one_contact'],
                    player_one_hall=request.POST['player_one_hall'],
                    player_two_name=request.POST['player_two_name'],
                    player_two_email=request.POST['player_two_email'],
                    player_two_contact=request.POST['player_two_contact'],
                    player_two_hall=request.POST['player_two_hall'],
                    unique_team_id=unique_team_id
                )
                new_team.save()

                service.send_message(
                    team_name, unique_team_id, player_one_contact)
                service.send_message(
                    team_name, unique_team_id, player_two_contact)

                return render(request, 'success.html')

            else:
                is_team_name_taken = True
    else:
        form = RegistrationForm()

    context = {'form': form, 'is_team_name_taken': is_team_name_taken}
    return render(request, 'register.html', context)
