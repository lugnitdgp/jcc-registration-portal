from django import forms

class RegistrationForm(forms.Form):
    team_name = forms.CharField(label='Team Name' , max_length=255 , required = True , widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_one_name = forms.CharField(label='Player 1 Name' , max_length=255 , required = True , widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_one_email = forms.EmailField(label='Player 1 Email', max_length=255 , required = True , widget=forms.EmailInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_one_contact = forms.IntegerField(label='Player 1 Contact',required = True , widget=forms.NumberInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_one_hall = forms.IntegerField(label='Player 1 Hall Number',required=True , widget=forms.NumberInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_two_name = forms.CharField(label='Player 2 Name', max_length=255 , required = True , widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_two_email = forms.EmailField(label='Player 2 Email', max_length=255 , required = True , widget=forms.EmailInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_two_contact = forms.IntegerField(label='Player 2 Contact', required = True , widget=forms.NumberInput(attrs={'class':'form-control form-control-sm mb-2'}))
    player_two_hall = forms.IntegerField(label='Player 2 Hall Number', required=True , widget=forms.NumberInput(attrs={'class':'form-control form-control-sm mb-2'}))

