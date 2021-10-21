from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.




def projects(request):

     #name = 'Joshua West'
     projects = Project.objects.all()
   # print('PROJECTS: ' , projects)
     context = {'projects': projects}
     return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # reviews = projectObj.review_set.all()
    context = { 'project': projectObj ,'tags': tags, 'reviews': reviews}
    return render(request, 'projects/single-projects.html', context)



def createProject(request):
    
    form = ProjectForm()

    if request.method == 'POST':
        print('FORM DATA: ' , request.POST)
    context = {'form': form}
    return render (request, 'projects/project-form.html', context)        
