from django.forms import ModelForm
from UI.models import Client
from django import forms

# class CreateClientForm(forms.Form):
#     client_name = forms.CharField()
#     client_type = forms.ChoiceField()

class CreateClientModelForm(ModelForm):
   class Meta:
       model = Client
       fields = ['name', 'type']
