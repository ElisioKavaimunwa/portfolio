from django.shortcuts import render
from projects.models import Project

def project_index(request):
    template_name = "project_index.html"
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, template_name, context)

def project_detail(request, pk):
    template_name = "project_detail.html"
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, template_name, context)
