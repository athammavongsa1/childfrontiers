from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from UI.forms import CreateClientModelForm

from UI.models import Client, Employee, Project, Question, Vignette, DataSource


# Homepage view
def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

#Views for client
class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client_list')

class ClientUpdate(UpdateView):
    model = Client
    fields = ['name', 'type']

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')

class ClientDetailView(generic.DetailView):
    model = Client

class ClientListView(generic.ListView):
    model = Client

#Views for employee
class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'job_title']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')

class EmployeeDetailView(generic.DetailView):
    model = Employee

class EmployeeListView(generic.ListView):
    model = Employee
    
#Views for project
class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_list')

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'project_type', 'completion_date', 'country', 'client']

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectListView(generic.ListView):
    model = Project

#Views for question
class QuestionCreate(CreateView):
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('question_list')

class QuestionUpdate(UpdateView):
    model = Question
    fields = ['question_id', 'question_text', 'question_rank']

class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('question_list')

class QuestionDetailView(generic.DetailView):
    model = Question

class QuestionListView(generic.ListView):
    model = Question
    
#Views for vignette
class VignetteCreate(CreateView):
    model = Vignette
    fields = '__all__'
    success_url = reverse_lazy('vignette_list')

class VignetteUpdate(UpdateView):
    model = Vignette
    fields = ['vignette_type', 'vignette_description']

class VignetteDelete(DeleteView):
    model = Vignette
    success_url = reverse_lazy('vignette_list')

class VignetteDetailView(generic.DetailView):
    model = Vignette

class VignetteListView(generic.ListView):
    model = Vignette

#Views for data_source
class DataSourceCreate(CreateView):
    model = DataSource
    fields = '__all__'
    success_url = reverse_lazy('data_source_list')

class DataSourceUpdate(UpdateView):
    model = DataSource
    fields = ['data_source_type', 'acquisition_date', 'project', 'province', 'district', 'community']

class DataSourceDelete(DeleteView):
    model = DataSource
    success_url = reverse_lazy('data_source_list')

class DataSourceDetailView(generic.DetailView):
    model = DataSource

class DataSourceListView(generic.ListView):
    model = DataSource




# def create_client(request):
#     client_instance = Client()
#
#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#
#         # Create a form instance and populate it with data from the request (binding):
#         form = CreateClientModelForm(request.POST)
#
#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             client_instance.name = form.cleaned_data['name']
#             client_instance.type = form.cleaned_data['type']
#             client_instance.save()
#
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('index') )
#
#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = CreateClientModelForm()
#
#     context = {
#         'form': form,
#         'client_instance': client_instance,
#     }
#
#     return render(request, 'client_form.html', context)




