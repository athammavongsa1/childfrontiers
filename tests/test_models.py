from django.test import TestCase
from UI.models import Client, Project

# Test suite for models.

class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name='UNICEF', type='UN')

    def setUp(self):
        pass

    def test_name_label(self):
        client = Client.objects.get(client_id=1)
        field_label = client._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_type_label(self):
        client = Client.objects.get(client_id=1)
        field_label = client._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_name_max_length(self):
        client = Client.objects.get(client_id=1)
        max_length = client._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        client = Client.objects.get(client_id=1)
        expected_object_name = f'{client.name}'
        self.assertEquals(expected_object_name, str(client))

    def test_get_absolute_url(self):
        client = Client.objects.get(client_id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(client.get_absolute_url(), '/UI/client/1')

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(name='UNICEF', type='UN')
        Project.objects.create(name='Nigeria Study', project_type='research', completion_date='2013-01-13',
                               country='Vietnam', client_id=client)

    def setUp(self):
        pass

    def test_name_label(self):
        project = Project.objects.get(project_id=1)
        field_label = project._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_project_type_label(self):
        project = Project.objects.get(project_id=1)
        field_label = project._meta.get_field('project_type').verbose_name
        self.assertEquals(field_label, 'project_type')

    def test_completion_date_label(self):
        project = Project.objects.get(project_id=1)
        field_label = project._meta.get_field('completion_date').verbose_name
        self.assertEquals(field_label, 'completion_date')
    
    def test_country_label(self):
        project = Project.objects.get(project_id=1)
        field_label = project._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')

    # def test_client_label(self):
    #     project = Project.objects.get(project_id=1)
    #     field_label = project._meta.get_field('project_type').verbose_name
    #     self.assertEquals(field_label, 'project_type')
    #
    # def test_team_label(self):
    #     project = Project.objects.get(project_id=1)
    #     field_label = project._meta.get_field('team').verbose_name
    #     self.assertEquals(field_label, 'team')

    # def test_name_max_length(self):
    #     project = Project.objects.get(project_id=1)
    #     max_length = project._meta.get_field('name').max_length
    #     self.assertEquals(max_length, 100)
    #
    # def test_object_name_is_name(self):
    #     project = Project.objects.get(project_id=1)
    #     expected_object_name = f'{project.name}'
    #     self.assertEquals(expected_object_name, str(project))
    #
    # def test_get_absolute_url(self):
    #     project = Project.objects.get(project_id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEquals(project.get_absolute_url(), '/UI/project/1')
    #


