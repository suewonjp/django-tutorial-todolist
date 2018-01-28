from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def index(request):
    # return HttpResponse('Hello World')
    todos = Todo.objects.all()[:10]
    context = {
            'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
            'todo':todo
    }
    return render(request, 'details.html', context)

