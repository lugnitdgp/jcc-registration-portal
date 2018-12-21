from django import forms
from phonenumber_field.formfields import PhoneNumberField

HALL_CHOICES = [
    ('hall 1', 'Hall 1'),
    ('hall 2', 'Hall 2'),
    ('hall 3', 'Hall 3'),
    ('hall 5', 'Hall 5'),
    ('hall 6', 'Hall 6'),
    ('hall 7', 'Hall 7'),
    ('hall 11', 'Hall 11'),
    ('hall 13', 'Hall 13'),
    ('hall 14', 'Hall 14'),
]


class RegistrationForm(forms.Form):
    team_name = forms.CharField(label='Team Name', max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))
    player_one_name = forms.CharField(label='Player 1 Name', max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))
    player_one_email = forms.EmailField(label='Player 1 Email', max_length=255, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))
    player_one_contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),label=_("Player 1 Contact"), required=False)
    player_one_hall = forms.CharField(label='Player 1 Hall Number', required=True, widget=forms.Select(choices=HALL_CHOICES,
                                                                                                       attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))
    player_two_name = forms.CharField(label='Player 2 Name', max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))
    player_two_email = forms.EmailField(label='Player 2 Email', max_length=255, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))
    player_two_contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),label=_("Player 2 Contact"), required=False)
    player_two_hall = forms.CharField(label='Player 2 Hall Number', required=True, widget=forms.Select(choices=HALL_CHOICES,
                                                                                                       attrs={'class': 'form-control form-control-sm mb-2 text-dark'}))

