from django.contrib import admin
from UI.models import Client, DataSource, Employee, ProjectDataSourceEmployee, Participant, Project, Question, QuestionVignette, Response, Vignette

# Register model representations of database tables.
admin.site.register(Client)
admin.site.register(DataSource)
admin.site.register(Employee)
admin.site.register(ProjectDataSourceEmployee)
admin.site.register(Participant)
admin.site.register(Project)
admin.site.register(Question)
admin.site.register(QuestionVignette)
admin.site.register(Response)
admin.site.register(Vignette)

