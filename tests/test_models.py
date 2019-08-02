from django.test import TestCase
from UI.models import Client, Project, Employee, Participant, Question, Response, Vignette, DataSource


# Test suite for models.

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        ProjectModelTest.test_project_id = project.pk

    def test_name_label(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        field_label = project._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_project_type_label(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        field_label = project._meta.get_field('project_type').verbose_name
        self.assertEquals(field_label, 'project type')

    def test_completion_date_label(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        field_label = project._meta.get_field('completion_date').verbose_name
        self.assertEquals(field_label, 'completion date')

    def test_country_label(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        field_label = project._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')

    def test_client_label(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        field_label = project._meta.get_field('client').verbose_name
        self.assertEquals(field_label, 'client')

    def test_name_max_length(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        max_length = project._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        expected_object_name = f'{project.name}'
        self.assertEquals(expected_object_name, str(project))

    def test_get_absolute_url(self):
        project = Project.objects.get(project_id=ProjectModelTest.test_project_id)
        self.assertEquals(project.get_absolute_url(), '/UI/project/' + str(ProjectModelTest.test_project_id))


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        ClientModelTest.test_client_id = client.pk

    def test_name_label(self):
        client = Client.objects.get(client_id=ClientModelTest.test_client_id)
        field_label = client._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_type_label(self):
        client = Client.objects.get(client_id=ClientModelTest.test_client_id)
        field_label = client._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_name_max_length(self):
        client = Client.objects.get(client_id=ClientModelTest.test_client_id)
        max_length = client._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        client = Client.objects.get(client_id=ClientModelTest.test_client_id)
        expected_object_name = f'{client.name}'
        self.assertEquals(expected_object_name, str(client))

    def test_get_absolute_url(self):
        client = Client.objects.get(client_id=ClientModelTest.test_client_id)
        self.assertEquals(client.get_absolute_url(), '/UI/client/' + str(ClientModelTest.test_client_id))


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')
        EmployeeModelTest.test_employee_id = employee.pk

    def test_first_name_label(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        field_label = employee._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_employee_last_name_label(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        field_label = employee._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_job_title_label(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        field_label = employee._meta.get_field('job_title').verbose_name
        self.assertEquals(field_label, 'job title')

    def test_first_name_max_length(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        max_length = employee._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_last_name_max_length(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        max_length = employee._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_first_name(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        expected_object_name = f'{employee.last_name}, {employee.first_name}'
        self.assertEquals(expected_object_name, str(employee))

    def test_get_absolute_url(self):
        employee = Employee.objects.get(employee_id=EmployeeModelTest.test_employee_id)
        self.assertEquals(employee.get_absolute_url(), '/UI/employee/' + str(EmployeeModelTest.test_employee_id))


class ParticipantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        participant = Participant.objects.create(participant_type='NGO STAFF')
        ParticipantModelTest.test_participant_id = participant.pk

    def test_participant_type_label(self):
        participant = Participant.objects.get(participant_id=ParticipantModelTest.test_participant_id)
        field_label = participant._meta.get_field('participant_type').verbose_name
        self.assertEquals(field_label, 'participant type')

    def test_object_name_is_participant_type(self):
        participant = Participant.objects.get(participant_id=ParticipantModelTest.test_participant_id)
        expected_object_name = f'{participant.participant_type}'
        self.assertEquals(expected_object_name, str(participant))


class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(question_text='Who would you go to?', question_rank=1)
        QuestionModelTest.test_question_id = question.pk

        question_no_rank = Question.objects.create(question_text='Who would you go to? No rank')
        QuestionModelTest.test_question_no_rank_id = question_no_rank.pk

    def test_question_text_label(self):
        question = Question.objects.get(question_id=QuestionModelTest.test_question_id)
        field_label = question._meta.get_field('question_text').verbose_name
        self.assertEquals(field_label, 'question text')

    def test_question_rank_label(self):
        question = Question.objects.get(question_id=QuestionModelTest.test_question_id)
        field_label = question._meta.get_field('question_rank').verbose_name
        self.assertEquals(field_label, 'question rank')

    def test_question_text_max_length(self):
        question = Question.objects.get(question_id=QuestionModelTest.test_question_id)
        max_length = question._meta.get_field('question_text').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_question_type_rank(self):
        question = Question.objects.get(question_id=QuestionModelTest.test_question_id)
        expected_object_name = f'{question.question_text} rank: {question.question_rank}'
        self.assertEquals(expected_object_name, str(question))

    def test_object_name_is_question_type_no_rank(self):
        question_no_rank = Question.objects.get(question_id=QuestionModelTest.test_question_no_rank_id)
        expected_object_name_no_rank = f'{question_no_rank.question_text}'
        self.assertEquals(expected_object_name_no_rank, str(question_no_rank))

    def test_get_absolute_url(self):
        question = Question.objects.get(question_id=QuestionModelTest.test_question_id)
        self.assertEquals(question.get_absolute_url(), '/UI/question/' + str(QuestionModelTest.test_question_id))


class VignetteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        vignette = Vignette.objects.create(vignette_type='neglect', vignette_description='test description')
        VignetteModelTest.test_vignette_id = vignette.pk

    def test_vignette_type_label(self):
        vignette = Vignette.objects.get(vignette_id=VignetteModelTest.test_vignette_id)
        field_label = vignette._meta.get_field('vignette_type').verbose_name
        self.assertEquals(field_label, 'vignette type')

    def test_vignette_description_label(self):
        vignette = Vignette.objects.get(vignette_id=VignetteModelTest.test_vignette_id)
        field_label = vignette._meta.get_field('vignette_description').verbose_name
        self.assertEquals(field_label, 'vignette description')

    def test_vignette_description_max_length(self):
        vignette = Vignette.objects.get(vignette_id=VignetteModelTest.test_vignette_id)
        max_length = vignette._meta.get_field('vignette_description').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_vignette_description(self):
        vignette = Vignette.objects.get(vignette_id=VignetteModelTest.test_vignette_id)
        expected_object_name = f'{vignette.vignette_description}'
        self.assertEquals(expected_object_name, str(vignette))

    def test_get_absolute_url(self):
        vignette = Vignette.objects.get(vignette_id=VignetteModelTest.test_vignette_id)
        self.assertEquals(vignette.get_absolute_url(), '/UI/vignette/' + str(VignetteModelTest.test_vignette_id))


class DataSourceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        data_source = DataSource.objects.create(name='Nigeria Study', data_source_type='focus group',
                                                acquisition_date='2013-03-30',
                                                project=project, province='Columbia', district='Jackson',
                                                community='Sylva')
        DataSourceModelTest.test_data_source_id = data_source.pk

    def test_name_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_data_source_type_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('data_source_type').verbose_name
        self.assertEquals(field_label, 'data source type')

    def test_acquisition_date_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('acquisition_date').verbose_name
        self.assertEquals(field_label, 'acquisition date')

    def test_project_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('project').verbose_name
        self.assertEquals(field_label, 'project')

    def test_province_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('province').verbose_name
        self.assertEquals(field_label, 'province')

    def test_district_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('district').verbose_name
        self.assertEquals(field_label, 'district')

    def test_community_label(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        field_label = data_source._meta.get_field('community').verbose_name
        self.assertEquals(field_label, 'community')

    def test_name_max_length(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        max_length = data_source._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_province_max_length(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        max_length = data_source._meta.get_field('province').max_length
        self.assertEquals(max_length, 50)

    def test_district_max_length(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        max_length = data_source._meta.get_field('district').max_length
        self.assertEquals(max_length, 50)

    def test_community_max_length(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        max_length = data_source._meta.get_field('community').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        expected_object_name = f'{data_source.name}'
        self.assertEquals(expected_object_name, str(data_source))

    def test_get_absolute_url(self):
        data_source = DataSource.objects.get(data_source_id=DataSourceModelTest.test_data_source_id)
        self.assertEquals(data_source.get_absolute_url(), '/UI/data_source/' +
                          str(DataSourceModelTest.test_data_source_id))


class ResponseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        data_source = DataSource.objects.create(name='Nigeria Study', data_source_type='focus group',
                                                acquisition_date='2013-03-30',
                                                project=project, province='Columbia', district='Jackson',
                                                community='Sylva')
        question = Question.objects.create(question_text='Who would you go to?', question_rank=1)
        participant = Participant.objects.create(participant_type='NGO STAFF')

        response = Response.objects.create(qualitative_response="Yes", participant=participant, question=question,
                                           data_source=data_source)
        ResponseModelTest.test_response_id = response.pk

    def test_qual_response_label(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        field_label = response._meta.get_field('qualitative_response').verbose_name
        self.assertEquals(field_label, 'qualitative response')

    def test_quant_response_label(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        field_label = response._meta.get_field('quantitative_response').verbose_name
        self.assertEquals(field_label, 'quantitative response')

    def test_boolean_response_label(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        field_label = response._meta.get_field('boolean_response').verbose_name
        self.assertEquals(field_label, 'boolean response')

    def test_participant_label(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        field_label = response._meta.get_field('participant').verbose_name
        self.assertEquals(field_label, 'participant')

    def test_question_label(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        field_label = response._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'question')

    def test_data_source_label(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        field_label = response._meta.get_field('data_source').verbose_name
        self.assertEquals(field_label, 'data source')

    def test_qual_response_max_length(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        max_length = response._meta.get_field('qualitative_response').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_response(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        expected_object_name = f'{response.qualitative_response}'
        self.assertEquals(expected_object_name, str(response))

    def test_get_absolute_url(self):
        response = Response.objects.get(response_id=ResponseModelTest.test_response_id)
        self.assertEquals(response.get_absolute_url(), '/UI/response/' + str(ResponseModelTest.test_response_id))
