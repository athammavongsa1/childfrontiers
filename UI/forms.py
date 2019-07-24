from django.forms import ModelForm, ModelChoiceField
from UI.models import Client, Employee, Project, Question, Vignette, DataSource, Participant, Response


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


class CreateResponseModelForm(ModelForm):
    participant = ModelChoiceField(queryset=Participant.objects.all(), to_field_name='participant_type',
                                   empty_label="Select participant")
    question = ModelChoiceField(queryset=Question.objects.all(), to_field_name='question_text', empty_label="Select question")
    data_source = ModelChoiceField(queryset=DataSource.objects.all(), to_field_name='name',
                                   empty_label="Select data source")

    class Meta:
        model = Response
        fields = ['qualitative_response', 'quantitative_response', 'boolean_response', 'participant', 'question',
                  'data_source']
