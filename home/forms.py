from django.forms import ModelForm
from django import forms
from . models import TicketModel


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput)

class TicketForm(forms.ModelForm):

    class Meta:
        model = TicketModel
        fields = ['Title', 'Description', 'priority', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['priority'].default = None
