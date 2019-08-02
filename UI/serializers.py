from UI.models import Client, Project, Employee, Participant, Question, Response, Vignette, DataSource
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'type']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_title']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = Project
        fields = ['name', 'project_type', 'completion_date', 'country', 'client']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'question_rank']


class VignetteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vignette
        fields = ['vignette_type', 'vignette_description']


class DataSourceSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = DataSource
        fields = ['name', 'data_source_type', 'acquisition_date', 'project', 'province', 'district', 'community']


class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    participant = serializers.SlugRelatedField(many=False, read_only=True, slug_field='participant_type')
    question = serializers.SlugRelatedField(many=False, read_only=True, slug_field='question_text')
    data_source = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = Response
        fields = ['qualitative_response', 'quantitative_response', 'boolean_response', 'participant', 'question',
                  'data_source']
