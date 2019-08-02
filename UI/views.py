from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from UI.models import Client, Employee, Project, Question, Vignette, DataSource, Response
from UI.serializers import ClientSerializer, EmployeeSerializer, ProjectSerializer, QuestionSerializer, \
    VignetteSerializer, DataSourceSerializer, ResponseSerializer


# View for welcome page.
def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


# View for create client page.
class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client_list')

    def get_context_data(self, **kwargs):
        context = super(ClientCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update client page.
class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ClientUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete client page.
class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')


# View for client detail page.
class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client

    def project(self):
        return Project.objects.all()


# View for list clients page.
class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    paginate_by = 12

# View for client serializer
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer


# View for create employee page.
class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee_list')

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update employee page.
class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete employee page.
class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')


# View for employee detail page.
class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee


# View for list employees page.
class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    paginate_by = 12

# View for employee serializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('last_name')
    serializer_class = EmployeeSerializer


# View for create project page.
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_list')

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update project page.
class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete project page.
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')


# View for project detail page.
class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project

    def data_source(self):
        return DataSource.objects.all()

# View for list projects page.
class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 12

# View for project serializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer


# View for create question page.
class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('question_list')

    def get_context_data(self, **kwargs):
        context = super(QuestionCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update question page.
class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete question page.
class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('question_list')


# View for question detail page.
class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Question


# View for list questions page.
class QuestionListView(LoginRequiredMixin, generic.ListView):
    model = Question
    paginate_by = 12

# View for question serializer
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('question_text')
    serializer_class = QuestionSerializer

# View for create vignette page.
class VignetteCreate(LoginRequiredMixin, CreateView):
    model = Vignette
    fields = '__all__'
    success_url = reverse_lazy('vignette_list')

    def get_context_data(self, **kwargs):
        context = super(VignetteCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update vignette page.
class VignetteUpdate(LoginRequiredMixin, UpdateView):
    model = Vignette
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(VignetteUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete vignette page.
class VignetteDelete(LoginRequiredMixin, DeleteView):
    model = Vignette
    success_url = reverse_lazy('vignette_list')


# View for vignette detail page.
class VignetteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vignette


# View for list vignettes page.
class VignetteListView(LoginRequiredMixin, generic.ListView):
    model = Vignette
    paginate_by = 12

# View for vignette serializer
class VignetteViewSet(viewsets.ModelViewSet):
    queryset = Vignette.objects.all().order_by('vignette_description')
    serializer_class = VignetteSerializer

# View for create data source page.
class DataSourceCreate(LoginRequiredMixin, CreateView):
    model = DataSource
    fields = '__all__'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.project_id})

    def get_context_data(self, **kwargs):
        context = super(DataSourceCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update data source page.
class DataSourceUpdate(LoginRequiredMixin, UpdateView):
    model = DataSource
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DataSourceUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete data source page.
class DataSourceDelete(LoginRequiredMixin, DeleteView):
    model = DataSource
    success_url = reverse_lazy('data_source_list')


# View for data source detail page.
class DataSourceDetailView(LoginRequiredMixin, generic.DetailView):
    model = DataSource

    def response(self):
        return Response.objects.all()


# View for list data sources page.
class DataSourceListView(LoginRequiredMixin, generic.ListView):
    model = DataSource
    paginate_by = 12

# View for data source serializer
class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all().order_by('name')
    serializer_class = DataSourceSerializer

# View for create response page.
class ResponseCreate(LoginRequiredMixin, CreateView):
    model = Response
    fields = '__all__'

    def get_success_url(self):
        return reverse('data_source_detail', kwargs={'pk': self.object.data_source.data_source_id})

    def get_context_data(self, **kwargs):
        context = super(ResponseCreate, self).get_context_data(**kwargs)
        context['get_redirect'] = 1
        return context


# View for update response page.
class ResponseUpdate(LoginRequiredMixin, UpdateView):
    model = Response
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ResponseUpdate, self).get_context_data(**kwargs)
        context['get_redirect'] = 0
        return context


# View for delete response page.
class ResponseDelete(LoginRequiredMixin, DeleteView):
    model = Response
    success_url = reverse_lazy('response_list')


# View for response detail page.
class ResponseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Response


# View for list responses page.
class ResponseListView(LoginRequiredMixin, generic.ListView):
    model = Response
    paginate_by = 12

# View for response serializer
class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all().order_by('response_id')
    serializer_class = ResponseSerializer
