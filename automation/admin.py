from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Profession)
admin.site.register(Position)
admin.site.register(PositionCount)
admin.site.register(ProfessionCount)
admin.site.register(DailyReport)
admin.site.register(Material)
admin.site.register(MaterialCount)
admin.site.register(Unit)
admin.site.register(Equipe)
admin.site.register(EquipeCount)
admin.site.register(Contractor)
admin.site.register(ContractorCount)
admin.site.register(Zone)
admin.site.register(Task)
admin.site.register(ParentTask)
admin.site.register(TaskReport)
#
admin.site.register(Operation)
admin.site.register(SubOperation)
admin.site.register(ZoneOperation)


admin.site.register(MyUser)
admin.site.register(Project)

admin.site.register(IssueReport)
admin.site.register(Issue)
admin.site.register(IssueCount)
