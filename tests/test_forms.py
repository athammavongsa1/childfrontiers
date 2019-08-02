from django.test import TestCase
from UI.forms import CreateClientModelForm, CreateDataSourceModelForm, CreateEmployeeModelForm, CreateProjectModelForm, \
    CreateQuestionModelForm, CreateResponseModelForm, CreateVignetteModelForm

# Test suite for forms.
class CreateClientFormTest(TestCase):
    def test_name_label(self):
        form = CreateClientModelForm()
        self.assertTrue(form.fields['name'].label == 'Name')

    def test_type_label(self):
        form = CreateClientModelForm()
        self.assertTrue(form.fields['type'].label == 'Type')

class CreateEmployeeFormTest(TestCase):
    def test_first_name_label(self):
        form = CreateEmployeeModelForm()
        self.assertTrue(form.fields['first_name'].label == 'First name')

    def test_last_name_label(self):
        form = CreateEmployeeModelForm()
        self.assertTrue(form.fields['last_name'].label == 'Last name')

    def test_job_title_label(self):
        form = CreateEmployeeModelForm()
        self.assertTrue(form.fields['job_title'].label == 'Job title')

class CreateProjectFormTest(TestCase):
    def test_name_label(self):
        form = CreateProjectModelForm()
        self.assertTrue(form.fields['name'].label == 'Name')

    def test_type_label(self):
        form = CreateProjectModelForm()
        self.assertTrue(form.fields['project_type'].label == 'Project type')

    def test_completion_date_label(self):
        form = CreateProjectModelForm()
        self.assertTrue(form.fields['completion_date'].label == 'Completion date')

class CreateQuestionFormTest(TestCase):
    def test_text_label(self):
        form = CreateQuestionModelForm()
        self.assertTrue(form.fields['question_text'].label == 'Question text')

    def test_rank_label(self):
        form = CreateQuestionModelForm()
        self.assertTrue(form.fields['question_rank'].label == 'Question rank')

class CreateVignetteFormTest(TestCase):
    def test_type_label(self):
        form = CreateVignetteModelForm()
        self.assertTrue(form.fields['vignette_type'].label == 'Vignette type')

    def test_description_label(self):
        form = CreateVignetteModelForm()
        self.assertTrue(form.fields['vignette_description'].label == 'Vignette description')

class CreateDataSourceFormTest(TestCase):
    def test_name_label(self):
        form = CreateDataSourceModelForm()
        self.assertTrue(form.fields['name'].label == 'Name')

    def test_type_label(self):
        form = CreateDataSourceModelForm()
        self.assertTrue(form.fields['data_source_type'].label == 'Data source type')

    def test_date_label(self):
        form = CreateDataSourceModelForm()
        self.assertTrue(form.fields['acquisition_date'].label == 'Acquisition date')

    def test_province_label(self):
        form = CreateDataSourceModelForm()
        self.assertTrue(form.fields['province'].label == 'Province')

    def test_district_label(self):
        form = CreateDataSourceModelForm()
        self.assertTrue(form.fields['district'].label == 'District')

    def test_community_label(self):
        form = CreateDataSourceModelForm()
        self.assertTrue(form.fields['community'].label == 'Community')

class CreateResonseFormTest(TestCase):
    def test_qual_label(self):
        form = CreateResponseModelForm()
        self.assertTrue(form.fields['qualitative_response'].label == 'Qualitative response')

    def test_quant_label(self):
        form = CreateResponseModelForm()
        self.assertTrue(form.fields['quantitative_response'].label == 'Quantitative response')

    def test_bool_label(self):
        form = CreateResponseModelForm()
        self.assertTrue(form.fields['boolean_response'].label == 'Boolean response')

