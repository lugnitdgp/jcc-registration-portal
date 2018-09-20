from django import forms

class RegistrationForm(forms.Form):
    team_name = forms.CharField(label='Team Name' , max_length=255 , required = True , widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_one_name = forms.CharField(label='Player 1 Name' , max_length=255 , required = True , widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_two_name = forms.CharField(label='Player 2 Name', max_length=255 , required = True , widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
