from django.contrib import admin

# Register your models here.
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'description','image') 
    list_filter = ['title']
    search_fields = ['title']

    
admin.site.register(Project, ProjectAdmin)