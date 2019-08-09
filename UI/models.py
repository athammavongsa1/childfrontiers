# This is an auto-generated Django model module that creates modules for database entitites.

from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# A class to create client objects.
class Client(models.Model):
    client_types = (
        ('government', 'government'),
        ('NGO', 'NGO'),
        ('UN', 'UN'),
        ('foundation', 'foundation'),
        ('private sector', 'private_sector')
    )

    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=50, choices=client_types, blank=False, null=False)

    # A function to send url requests to client detail page.
    def get_absolute_url(self):
        return reverse('client_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of a client in the form of the client name.
    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed = False
        db_table = 'client'
        ordering = ('name',)


# A class to create project objects.
class Project(models.Model):
    project_types = (('research', 'research'), ('evaluation', 'evaluation'), ('system mapping', 'system mapping'),
                     ('technical assistance', 'technical assistance'))
    project_countries = (('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'),
                         ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'),
                         ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'),
                         ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'),
                         ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'),
                         ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'),
                         ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'),
                         ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'),
                         ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'),
                         ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cote dIvoire', 'Cote dIvoire'),
                         ('Cabo Verde', 'Cabo Verde'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'),
                         ('Canada', 'Canada'), ('Central African Republic', 'Central African Republic'),
                         ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'),
                         ('Comoros', 'Comoros'), ('Congo (Congo-Brazzaville)', 'Congo (Congo-Brazzaville)'),
                         ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'),
                         ('Czechia', 'Czechia'),
                         ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
                         ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'),
                         ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'),
                         ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'),
                         ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'),
                         ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'),
                         ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'),
                         ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'),
                         ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'),
                         ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'),
                         ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'),
                         ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'),
                         ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'),
                         ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'),
                         ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'),
                         ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'),
                         ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Madagascar', 'Madagascar'),
                         ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'),
                         ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'),
                         ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia', 'Micronesia'),
                         ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'),
                         ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'),
                         ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'),
                         ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'),
                         ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Korea', 'North Korea'),
                         ('North Macedonia', 'North Macedonia'), ('Norway', 'Norway'), ('Oman', 'Oman'),
                         ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Palestine State', 'Palestine State'),
                         ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'),
                         ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'),
                         ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russia', 'Russia'),
                         ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
                         ('Saint Lucia', 'Saint Lucia'),
                         ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
                         ('Samoa', 'Samoa'), ('San Marino', 'San Marino'),
                         ('Sao Tome and Principe', 'Sao Tome and Principe'),
                         ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'),
                         ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'),
                         ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'),
                         ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'),
                         ('South Africa', 'South Africa'), ('South Korea', 'South Korea'),
                         ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'),
                         ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'),
                         ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'),
                         ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'),
                         ('Timor-Leste', 'Timor-Leste'), ('Togo', 'Togo'), ('Tonga', 'Tonga'),
                         ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'),
                         ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'),
                         ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'),
                         ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'),
                         ('United States of America', 'United States of America'), ('Uruguay', 'Uruguay'),
                         ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'),
                         ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe'))

    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=project_types, blank=False, null=False)
    completion_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=50, choices=project_countries, blank=False, null=False)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    team = models.ManyToManyField('Employee', through='ProjectDataSourceEmployee')

    # A function to send url requests to project detail page.
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of a project in the form of the project name.
    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed = False
        db_table = 'project'
        ordering = ('name',)


# A class to create data source objects.
class DataSource(models.Model):
    data_source_types = (('focus group', 'focus group'), ('survey', 'survey'))

    data_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    data_source_type = models.CharField(max_length=19, choices=data_source_types, blank=False, null=False)
    acquisition_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    province = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    team = models.ManyToManyField('Employee', through='ProjectDataSourceEmployee')

    # A function to send url requests to data source detail page.
    def get_absolute_url(self):
        return reverse('data_source_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of a data source in the form of the data source name.
    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed = False
        db_table = 'data_source'
        ordering = ('name',)


# A class to create employee objects.
class Employee(models.Model):
    job_title_types = (('Director', 'Director'),
                       ('Senior Associate', 'Senior Associate'),
                       ('Collaborator', 'Collaborator'),
                       ('Head of Knowledge Management and Innovation', 'Head of Knowledge Management and Innovation'),
                       ('Head of Research and Evaluation', 'Head of Research and Evaluation'),
                       ('National Researcher', 'National Researcher'))

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    job_title = models.CharField(max_length=50, choices=job_title_types, blank=False, null=False)

    # A function to send url requests to employee detail page.
    def get_absolute_url(self):
        return reverse('employee_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of an employee in the form of the employee name.
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        managed = False
        db_table = 'employee'
        ordering = ('last_name',)


# A class to create participant objects.
class Participant(models.Model):
    participant_types = (('CHILDREN GIRLS', 'CHILDREN GIRLS'), ('GIRLS', 'GIRLS'), ('BOYS', 'BOYS'), ('WOMEN', 'WOMEN'),
                         ('ADOLESCENT GIRLS', 'ADOLESCENT GIRLS'), ('CHILD GIRLS', 'CHILD GIRLS'), ('MEN', 'MEN'),
                         ('ADOLESCENT BOYS', 'ADOLESCENT BOYS'), ('CHILD BOYS', 'CHILD BOYS'),
                         ('FRONTLINE WORKERS', 'FRONTLINE WORKERS'), ('LOCAL AUTHORITIES', 'LOCAL AUTHORITIES'),
                         ('CHILD PROTECTION NETWORK', 'CHILD PROTECTION NETWORK'), ('SOCIAL WORKER', 'SOCIAL WORKER'),
                         ('PARA SOCIAL WORKER', 'PARA SOCIAL WORKER'), ('NGO STAFF', 'NGO STAFF'),
                         ('GOVERNMENT OFFICIAL', 'GOVERNMENT OFFICIAL'), ('ADULT WOMEN', 'ADULT WOMEN'),
                         ('ADULT MEN', 'ADULT MEN'), ('CHILDREN MIX', 'CHILDREN MIX'), ('FATHERS','FATHERS'),
                         ('MOTHERS','MOTHERS')
                         )

    participant_id = models.AutoField(primary_key=True)
    participant_type = models.CharField(max_length=30, choices=participant_types, blank=False, null=False)

    # A function to return a string representation of a participant in the form of the participant type.
    def __str__(self):
        return '%s' % self.participant_type

    class Meta:
        managed = False
        db_table = 'participant'


# A class to create ProjectDataSourceEmployee objects.
class ProjectDataSourceEmployee(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_data_source_employee'


# A class to create question objects.
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=255, blank=False, null=False)
    question_rank = models.IntegerField(blank=True, null=True)
    vignettes = models.ManyToManyField('Vignette', through='QuestionVignette')

    # A function to send url requests to question detail page.
    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of a question in the form of the question text and rank if entered.
    def __str__(self):
        if (self.question_rank):
            return '%s rank: %s' % (self.question_text, self.question_rank)
        else:
            return '%s' % (self.question_text)

    class Meta:
        managed = False
        db_table = 'question'
        ordering = ('question_text',)


# A class to create QuestionVignette objects.
class QuestionVignette(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    vignette = models.ForeignKey('Vignette', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'question_vignette'


# A class to create response objects.
class Response(models.Model):
    response_id = models.AutoField(primary_key=True)
    qualitative_response = models.CharField(max_length=255, blank=True, null=True)
    quantitative_response = models.IntegerField(blank=True, null=True)
    boolean_response = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)],
                                                   blank=True, null=True)
    participant = models.ForeignKey(Participant, models.DO_NOTHING)
    question = models.ForeignKey(Question, models.DO_NOTHING)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING)

    # A function to send url requests to response detail page.
    def get_absolute_url(self):
        return reverse('response_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of a response in the form of the response content.
    def __str__(self):
        if self.qualitative_response is not None:
            return '%s' % (self.qualitative_response)
        elif self.quantitative_response is not None:
            return '%d' % (self.quantitative_response)
        else:
            return '%d' % (self.boolean_response)

    class Meta:
        managed = False
        db_table = 'response'
        ordering = ('response_id',)


# A class to create vignette objects.
class Vignette(models.Model):
    vignette_types = (('sexual exploitation', 'sexual exploitation',), ('child marriage', 'child marriage'),
                      ('domestic violence', 'domestic violence'), ('neglect', 'neglect'))

    vignette_id = models.AutoField(primary_key=True)
    vignette_type = models.CharField(max_length=50, choices=vignette_types, blank=False, null=False)
    vignette_description = models.CharField(max_length=255, blank=False, null=False)

    # A function to send url requests to vignette detail page.
    def get_absolute_url(self):
        return reverse('vignette_detail', kwargs={'pk': self.pk})

    # A function to return a string representation of a vignette in the form of the vignette description.
    def __str__(self):
        return '%s' % self.vignette_description

    class Meta:
        managed = False
        db_table = 'vignette'
        ordering = ('vignette_description',)
