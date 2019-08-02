from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from UI.models import Client, Project, Employee, Participant, Question, Response, Response, DataSource


# Test suite for views.

class ClientListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name='UNICEF', type='UN')
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('client_list'))
        self.assertRedirects(response, '/accounts/login/?next=/UI/client/list')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('client_list'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/client_list.html')


class ClientDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        ClientDetailViewTest.test_client_id = client.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('client_detail', kwargs={'pk': ClientDetailViewTest.test_client_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/client/' + str(ClientDetailViewTest.test_client_id))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('client_detail', kwargs={'pk': ClientDetailViewTest.test_client_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/client_detail.html')


class ClientDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        ClientDeleteViewTest.test_client_id = client.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/client/' + str(ClientDeleteViewTest.test_client_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('client_delete', kwargs={'pk': ClientDeleteViewTest.test_client_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('client_delete', kwargs={'pk': ClientDeleteViewTest.test_client_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/client_confirm_delete.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('client_delete', kwargs={'pk': ClientDeleteViewTest.test_client_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/client/' + str(ClientDeleteViewTest.test_client_id) +
                             '/delete/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('client_delete', kwargs={'pk': ClientDeleteViewTest.test_client_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/client_confirm_delete.html')


class ProjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                               country='Vietnam', client=client)
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('project_list'))
        self.assertRedirects(response, '/accounts/login/?next=/UI/project/list')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('project_list'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/project_list.html')


class ProjectDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        ProjectDetailViewTest.test_project_id = project.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/project/' + str(ProjectDetailViewTest.test_project_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('project_detail', kwargs={'pk': ProjectDetailViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project_detail', kwargs={'pk': ProjectDetailViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/project_detail.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('project_detail', kwargs={'pk': ProjectDetailViewTest.test_project_id}))
        self.assertRedirects(response,
                             '/accounts/login/?next=/UI/project/' + str(ProjectDetailViewTest.test_project_id))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('project_detail', kwargs={'pk': ProjectDetailViewTest.test_project_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/project_detail.html')


class ProjectDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        ProjectDeleteViewTest.test_project_id = project.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/project/' + str(ProjectDeleteViewTest.test_project_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('project_delete', kwargs={'pk': ProjectDeleteViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project_delete', kwargs={'pk': ProjectDeleteViewTest.test_project_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/project_confirm_delete.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('project_delete', kwargs={'pk': ProjectDeleteViewTest.test_project_id}))
        self.assertRedirects(response,
                             '/accounts/login/?next=/UI/project/' + str(ProjectDeleteViewTest.test_project_id) +
                             '/delete/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('project_delete', kwargs={'pk': ProjectDeleteViewTest.test_project_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
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
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('data_source_list'))
        self.assertRedirects(response, '/accounts/login/?next=/UI/data_source/list')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('data_source_list'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/datasource_list.html')


class DataSourceDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        data_source = DataSource.objects.create(name='Nigeria Study', data_source_type='focus group',
                                                acquisition_date='2013-03-30', project=project, province='Columbia',
                                                district='Jackson', community='Sylva')
        DataSourceDetailViewTest.test_data_source_id = data_source.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/data_source/' + str(DataSourceDetailViewTest.test_data_source_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('data_source_detail',
                                           kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('data_source_detail',
                                           kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/datasource_detail.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('data_source_detail',
                                           kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/data_source/' +
                             str(DataSourceDetailViewTest.test_data_source_id))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('data_source_detail',
                                           kwargs={'pk': DataSourceDetailViewTest.test_data_source_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/datasource_detail.html')


class DataSourceDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        project = Project.objects.create(name='Nigeria Study', project_type='research',
                                         completion_date='2013-01-13',
                                         country='Vietnam', client=client)
        data_source = DataSource.objects.create(name='Nigeria Study', data_source_type='focus group',
                                                acquisition_date='2013-03-30', project=project, province='Columbia',
                                                district='Jackson', community='Sylva')
        DataSourceDeleteViewTest.test_data_source_id = data_source.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/data_source/' + str(DataSourceDeleteViewTest.test_data_source_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('data_source_delete',
                                           kwargs={'pk': DataSourceDeleteViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('data_source_delete',
                                           kwargs={'pk': DataSourceDeleteViewTest.test_data_source_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/datasource_confirm_delete.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('data_source_delete',
                                           kwargs={'pk': DataSourceDeleteViewTest.test_data_source_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/data_source/' +
                             str(DataSourceDeleteViewTest.test_data_source_id) +
                             '/delete/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('data_source_delete',
                                           kwargs={'pk': DataSourceDeleteViewTest.test_data_source_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/datasource_confirm_delete.html')


class EmployeeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('employee_list'))
        self.assertRedirects(response, '/accounts/login/?next=/UI/employee/list')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('employee_list'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/employee_list.html')


class EmployeeDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')
        EmployeeDetailViewTest.test_employee_id = employee.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('employee_detail', kwargs={'pk': EmployeeDetailViewTest.test_employee_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/employee/' +
                             str(EmployeeDetailViewTest.test_employee_id))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('employee_detail', kwargs={'pk': EmployeeDetailViewTest.test_employee_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/employee_detail.html')


class EmployeeDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = Employee.objects.create(first_name='Alex', last_name='Rampart', job_title='Director')
        EmployeeDeleteViewTest.test_employee_id = employee.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/employee/' + str(EmployeeDeleteViewTest.test_employee_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('employee_delete', kwargs={'pk': EmployeeDeleteViewTest.test_employee_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('employee_delete', kwargs={'pk': EmployeeDeleteViewTest.test_employee_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/employee_confirm_delete.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('employee_delete', kwargs={'pk': EmployeeDeleteViewTest.test_employee_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/employee/' +
                             str(EmployeeDeleteViewTest.test_employee_id) + '/delete/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('employee_delete', kwargs={'pk': EmployeeDeleteViewTest.test_employee_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/employee_confirm_delete.html')


class QuestionListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(question_text='Who would you go to?', question_rank=1)
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('question_list'))
        self.assertRedirects(response, '/accounts/login/?next=/UI/question/list')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('question_list'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/question_list.html')


class QuestionDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(question_text='Who would you go to?', question_rank=1)
        QuestionDetailViewTest.test_question_id = question.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/question/' + str(QuestionDetailViewTest.test_question_id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('question_detail', kwargs={'pk': QuestionDetailViewTest.test_question_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('question_detail', kwargs={'pk': QuestionDetailViewTest.test_question_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/question_detail.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('question_detail', kwargs={'pk': QuestionDetailViewTest.test_question_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/question/' +
                             str(QuestionDetailViewTest.test_question_id))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('question_detail', kwargs={'pk': QuestionDetailViewTest.test_question_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/question_detail.html')


class QuestionDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(question_text='Who would you go to?', question_rank=1)
        QuestionDeleteViewTest.test_question_id = question.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('question_delete', kwargs={'pk': QuestionDeleteViewTest.test_question_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/question/' +
                             str(QuestionDeleteViewTest.test_question_id) + '/delete/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('question_delete', kwargs={'pk': QuestionDeleteViewTest.test_question_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
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
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('response_list'))
        self.assertRedirects(response, '/accounts/login/?next=/UI/response/list')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('response_list'))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
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
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

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

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('response_detail', kwargs={'pk': ResponseDetailViewTest.test_response_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/response/' +
                             str(ResponseDetailViewTest.test_response_id))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('response_detail', kwargs={'pk': ResponseDetailViewTest.test_response_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
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
        ResponseDeleteViewTest.test_response_id = response.pk
        test_user1 = User.objects.create_user(username='testuser1', password='password123')
        test_user1.save()

    def setUp(self):
        self.client.login(username='testuser1', password='password123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/UI/response/' + str(ResponseDeleteViewTest.test_response_id) + '/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('response_delete', kwargs={'pk': ResponseDeleteViewTest.test_response_id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('response_delete', kwargs={'pk': ResponseDeleteViewTest.test_response_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UI/response_confirm_delete.html')

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('response_delete', kwargs={'pk': ResponseDeleteViewTest.test_response_id}))
        self.assertRedirects(response, '/accounts/login/?next=/UI/response/' +
                             str(ResponseDeleteViewTest.test_response_id) + '/delete/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('response_delete', kwargs={'pk': ResponseDeleteViewTest.test_response_id}))

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'UI/response_confirm_delete.html')
