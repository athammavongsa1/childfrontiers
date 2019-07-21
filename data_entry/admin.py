from django.contrib import admin
from data_entry.models import Client, DataSource, Employee, EmployeeProject, Participant, Project, Question, QuestionVignette, Response, Vignette

# Register your models here.
admin.site.register(Client)
admin.site.register(DataSource)
admin.site.register(Employee)
admin.site.register(EmployeeProject)
admin.site.register(Participant)
admin.site.register(Project)
admin.site.register(Question)
admin.site.register(QuestionVignette)
admin.site.register(Response)
admin.site.register(Vignette)

