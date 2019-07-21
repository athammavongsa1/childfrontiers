from django.forms import ModelForm
from data_entry.models import Client
from django import forms

class CreateClientForm(forms.Form):
    client_name = forms.CharField()
    client_type = forms.CharField()

