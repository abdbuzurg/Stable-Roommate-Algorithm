from django.contrib import admin
from . models import Survey

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pub_date')
    class Meta:
        model = Survey

admin.site.register(Survey, SurveyAdmin)
