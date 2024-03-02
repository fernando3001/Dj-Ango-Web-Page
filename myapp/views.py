from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from django.shortcuts import get_object_or_404, render

def hello(request, username):
    return HttpResponse(username)

def index(request):
    title = 'Welcome to Index Page!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    title = 'Welcome to About Page!'
    return render(request, 'index.html', {
        'title': title
    })

def projects(request):
    Projects = list(Project.objects.values())
    return JsonResponse(Projects, safe=False)

def tasks(request, id):
    tasks = get_object_or_404(Tasks, id=id)
    return HttpResponse(tasks.title)