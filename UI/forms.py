from django.forms import ModelForm, ModelChoiceField
from UI.models import Client, Employee, Project, Question, Vignette, DataSource


class CreateClientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'type']


class CreateEmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_title']


class CreateProjectModelForm(ModelForm):
    client = ModelChoiceField(queryset=Client.objects.all(), to_field_name='name', empty_label="Select client")

    class Meta:
        model = Project
        fields = ['name', 'project_type', 'completion_date', 'country', 'client']


class CreateQuestionModelForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'question_rank']


class CreateVignetteModelForm(ModelForm):
    class Meta:
        model = Vignette
        fields = ['vignette_type', 'vignette_description']


class CreateDataSourceModelForm(ModelForm):
    project = ModelChoiceField(queryset=Project.objects.all(), to_field_name='name', empty_label="Select project")

    class Meta:
        model = DataSource
        fields = ['name', 'data_source_type', 'acquisition_date', 'project', 'province', 'district', 'community']
