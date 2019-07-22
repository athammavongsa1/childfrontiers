from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# Adding paths for viewing and managing clients
urlpatterns += [
    path('client/create/', views.ClientCreate.as_view(), name='client_create'),
    path('client/<int:pk>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client_delete'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/list', views.ClientListView.as_view(), name='client_list')
]

