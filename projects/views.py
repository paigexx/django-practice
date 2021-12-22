from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_index(request):
    # query 
    projects = Project.objects.all()
    # send information to our template 
    context = {
        'projects': projects
    }
    # context added as param to project.html
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    # query one project via project key (pk)
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)