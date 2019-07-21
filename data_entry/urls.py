from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_client/', views.create_client, name='create-client'),
    path('clients/', views.ClientListView.as_view(), name='clients')
]