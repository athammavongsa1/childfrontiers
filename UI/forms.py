from django.forms import ModelForm, ModelChoiceField
from UI.models import Client, Employee, Project

class CreateClientModelForm(ModelForm):
   class Meta:
       model = Client
       fields = ['name', 'type']

class CreateEmployeeModelForm(ModelForm):
   class Meta:
       model = Employee
       fields = ['first_name', 'last_name', 'job_title']

class CreateProjectModelForm(ModelForm):
    client = ModelChoiceField(queryset=Client.objects.all(), to_field_name = 'name', empty_label="Select Client")

    class Meta:
       model = Project
       fields = ['name', 'project_type', 'completion_date', 'country', 'client']
