# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class DataSource(models.Model):
    data_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    data_source_type = models.CharField(max_length=19, blank=True, null=True)
    aquisition_date = models.DateField(blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_source'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=43)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeProject(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    project = models.ForeignKey('Project', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_project'


class Participant(models.Model):
    participant_id = models.AutoField(primary_key=True)
    participant_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participant'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    project_type = models.CharField(max_length=20, blank=True, null=True)
    completion_type = models.DateField()
    country = models.CharField(max_length=9)
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project'


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=255)
    question_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class QuestionVignette(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    vignette = models.ForeignKey('Vignette', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'question_vignette'


class Response(models.Model):
    response_id = models.AutoField(primary_key=True)
    qualitative_response = models.CharField(max_length=255)
    quantitative_response = models.IntegerField()
    boolean_response = models.IntegerField()
    participant = models.ForeignKey(Participant, models.DO_NOTHING)
    question = models.ForeignKey(Question, models.DO_NOTHING)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'response'


class Vignette(models.Model):
    vignette_id = models.AutoField(primary_key=True)
    vignette_type = models.CharField(max_length=19, blank=True, null=True)
    vignette_description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vignette'