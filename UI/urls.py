from django.urls import path
from UI import views

# Redirect base URL to index page
urlpatterns = [
    path('', views.index, name='index'),
]

# Add paths for viewing and managing clients
urlpatterns += [
    path('client/create/', views.ClientCreate.as_view(), name='client_create'),
    path('client/<int:pk>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client_delete'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/list', views.ClientListView.as_view(), name='client_list'),
    path('client/JSON', views.ClientJSON.as_view(), name='client_JSON'),
]

# Add paths for viewing and managing employees
urlpatterns += [
    path('employee/create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/list', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/JSON', views.EmployeeJSON.as_view(), name='employee_JSON'),
]

# Add paths for viewing and managing projects
urlpatterns += [
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/list', views.ProjectListView.as_view(), name='project_list'),
    path('project/JSON', views.ProjectJSON.as_view(), name='project_JSON'),
]

# Add paths for viewing and managing questions
urlpatterns += [
    path('question/create/', views.QuestionCreate.as_view(), name='question_create'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('question/list', views.QuestionListView.as_view(), name='question_list'),
    path('question/JSON', views.QuestionJSON.as_view(), name='question_JSON'),
]

# Add paths for viewing and managing vignettes
urlpatterns += [
    path('vignette/create/', views.VignetteCreate.as_view(), name='vignette_create'),
    path('vignette/<int:pk>/update/', views.VignetteUpdate.as_view(), name='vignette_update'),
    path('vignette/<int:pk>/delete/', views.VignetteDelete.as_view(), name='vignette_delete'),
    path('vignette/<int:pk>', views.VignetteDetailView.as_view(), name='vignette_detail'),
    path('vignette/list', views.VignetteListView.as_view(), name='vignette_list'),
    path('vignette/JSON', views.VignetteJSON.as_view(), name='vignette_JSON'),
]

# Add paths for viewing and managing data_sources
urlpatterns += [
    path('data_source/create/', views.DataSourceCreate.as_view(), name='data_source_create'),
    path('data_source/<int:pk>/update/', views.DataSourceUpdate.as_view(), name='data_source_update'),
    path('data_source/<int:pk>/delete/', views.DataSourceDelete.as_view(), name='data_source_delete'),
    path('data_source/<int:pk>', views.DataSourceDetailView.as_view(), name='data_source_detail'),
    path('data_source/list', views.DataSourceListView.as_view(), name='data_source_list'),
    path('data_source/JSON', views.DataSourceJSON.as_view(), name='data_source_JSON'),
]

# Add paths for viewing and managing responses
urlpatterns += [
    path('response/create/', views.ResponseCreate.as_view(), name='response_create'),
    path('response/<int:pk>/update/', views.ResponseUpdate.as_view(), name='response_update'),
    path('response/<int:pk>/delete/', views.ResponseDelete.as_view(), name='response_delete'),
    path('response/<int:pk>', views.ResponseDetailView.as_view(), name='response_detail'),
    path('response/list', views.ResponseListView.as_view(), name='response_list'),
    path('response/JSON', views.ResponseJSON.as_view(), name='response_JSON'),
]
