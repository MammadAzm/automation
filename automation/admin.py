from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Profession)
admin.site.register(Position)
admin.site.register(PositionCount)
admin.site.register(ProfessionCount)
admin.site.register(DailyReport)
