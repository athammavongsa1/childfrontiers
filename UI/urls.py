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

# Adding paths for viewing and managing employees
urlpatterns += [
    path('employee/create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/list', views.EmployeeListView.as_view(), name='employee_list')
]

# Adding paths for viewing and managing projects
urlpatterns += [
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/list', views.ProjectListView.as_view(), name='project_list')
]

