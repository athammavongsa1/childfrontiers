from django.test import TestCase
from django.urls import reverse
from UI.models import Client, Project, Employee, Participant, Question, Response, Response, DataSource


# Test suite for views.

class ClientListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name='UNICEF', type='UN')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/client/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/client_list.html')


class ClientDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        ClientDetailViewTest.test_client_id = client.pk


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/client/' + str(ClientDetailViewTest.test_client_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('client_detail', kwargs={'pk': ClientDetailViewTest.test_client_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('client_detail', kwargs={'pk': ClientDetailViewTest.test_client_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/client_detail.html')


class ClientDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        ClientDetailViewTest.test_client_id = client.pk

    def setUp(self):
        Client.objects.create(name='UNICEF', type='UN')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/client/' + str(ClientDetailViewTest.test_client_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('client_delete', kwargs={'pk': ClientDetailViewTest.test_client_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('client_delete', kwargs={'pk': ClientDetailViewTest.test_client_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/client_confirm_delete.html')


class ProjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                               country='Vietnam', client=client)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/project/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/project_list.html')


class ProjectDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                               country='Vietnam', client=client)
        ResponseDetailViewTest.test_project_id = project.pk

    def setUp(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/project/' + str(ResponseDetailViewTest.test_project_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('project_detail', kwargs={'pk': ResponseDetailViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project_detail', kwargs={'pk': ResponseDetailViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/project_detail.html')


class ProjectDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                               country='Vietnam', client=client)
        ResponseDetailViewTest.test_project_id = project.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/project/' + str(ResponseDetailViewTest.test_project_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('project_delete', kwargs={'pk': ResponseDetailViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project_delete', kwargs={'pk': ResponseDetailViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/project_confirm_delete.html')


class DataSourceListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        DataSource.objects.create(name='Nigeria Study', data_source_type='focus group', acquisition_date='2013-03-30',
                                  project=project, province='Columbia', district='Jackson', community='Sylva')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/data_source/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('data_source_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('data_source_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/datasource_list.html')


class DataSourceDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        data_source = DataSource.objects.create(name='Nigeria Study', data_source_type='focus group', acquisition_date='2013-03-30',
                                  project=project, province='Columbia', district='Jackson', community='Sylva')
        DataSourceDetailViewTest.test_data_source_id = data_source.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/data_source/' + str(DataSourceDetailViewTest.test_data_source_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('data_source_detail', kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('data_source_detail', kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/datasource_detail.html')


class DataSourceDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research',
                                         completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        data_source = DataSource.objects.create(name='Nigeria Study', data_source_type='focus group', acquisition_date='2013-03-30',
                                  project=project, province='Columbia', district='Jackson', community='Sylva')
        DataSourceDetailViewTest.test_data_source_id = data_source.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/data_source/' + str(DataSourceDetailViewTest.test_data_source_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('data_source_delete',
                                           kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('data_source_delete',
                                           kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/datasource_confirm_delete.html')


class EmployeeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/employee/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/employee_list.html')


class EmployeeDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')
        EmployeeDetailViewTest.test_employee_id = employee.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/employee/' + str(EmployeeDetailViewTest.test_employee_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee_detail', kwargs={'pk': EmployeeDetailViewTest.test_employee_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee_detail', kwargs={'pk': EmployeeDetailViewTest.test_employee_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/employee_detail.html')


class EmployeeDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')
        EmployeeDetailViewTest.test_employee_id = employee.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/employee/' + str(EmployeeDetailViewTest.test_employee_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee_delete', kwargs={'pk': EmployeeDetailViewTest.test_employee_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee_delete', kwargs={'pk': EmployeeDetailViewTest.test_employee_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/employee_confirm_delete.html')


class QuestionListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(question_text='Who would you go to?', question_rank=1)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/question/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/question_list.html')


class QuestionDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(question_text='Who would you go to?', question_rank=1)
        QuestionDeleteViewTest.test_question_id = question.pk


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/question/' + str(QuestionDeleteViewTest.test_question_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('question_detail', kwargs={'pk': QuestionDeleteViewTest.test_question_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('question_detail', kwargs={'pk': QuestionDeleteViewTest.test_question_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/question_detail.html')


class QuestionDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(question_text='Who would you go to?', question_rank=1)
        QuestionDeleteViewTest.test_question_id = question.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/question/' + str(QuestionDeleteViewTest.test_question_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('question_delete', kwargs={'pk': QuestionDeleteViewTest.test_question_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('question_delete', kwargs={'pk': QuestionDeleteViewTest.test_question_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/question_confirm_delete.html')


class ResponseListViewTest(TestCase):
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

        Response.objects.create(qualitative_response="Yes", participant=participant, question=question,
                                data_source=data_source)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/response/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('response_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('response_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/response_list.html')


class ResponseDetailViewTest(TestCase):
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
        ResponseDetailViewTest.test_response_id = response.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/response/' + str(ResponseDetailViewTest.test_response_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('response_detail', kwargs={'pk': ResponseDetailViewTest.test_response_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('response_detail', kwargs={'pk': ResponseDetailViewTest.test_response_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/response_detail.html')


class ResponseDeleteViewTest(TestCase):
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
        ResponseDetailViewTest.test_response_id = response.pk

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/response/' + str(ResponseDetailViewTest.test_response_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('response_delete', kwargs={'pk': ResponseDetailViewTest.test_response_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('response_delete', kwargs={'pk': ResponseDetailViewTest.test_response_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/response_confirm_delete.html')
