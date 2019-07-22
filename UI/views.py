from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from UI.forms import CreateClientModelForm

from UI.models import Client


# Homepage view
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_clients = Client.objects.all().count()

    context = {
        'num_clients': num_clients,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

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
    success_url = reverse_lazy('index')

class ClientDetailView(generic.DetailView):
    model = Client

class ClientListView(generic.ListView):
    model = Client

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




