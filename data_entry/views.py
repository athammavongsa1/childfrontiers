from django.views import generic

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from data_entry.forms import CreateClientForm

from data_entry.models import Client


# Create your views here.

def create_client(request):
    client_instance = Client()

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateClientForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            client_instance.name = form.cleaned_data['client_name']
            client_instance.type = form.cleaned_data['client_type']
            client_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateClientForm()

    context = {
        'form': form,
        'client_instance': client_instance,
    }

    return render(request, 'client_form.html', context)

class ClientListView(generic.ListView):
    model = Client

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_clients = Client.objects.all().count()

    context = {
        'num_clients': num_clients,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
