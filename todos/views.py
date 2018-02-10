from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
# from django.http import HttpResponse
from .models import Todo, Category

def index(request):
    todos = Todo.objects.all()[:10]
    context = {
            'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {
            'todo':todo,
            'categories':todo.category_set.all()
    }
    return render(request, 'details.html', context)

def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        categories = request.POST.getlist('category-select')
        if categories:
            for id in categories:
                category = Category.objects.get(id=id)
                todo.category_set.add(category)
        return redirect(reverse('todos:index'))
    else:
        categories = Category.objects.all()
        context = {
            'categories':categories
        }
        return render(request, 'add.html', context)

def update(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if (request.method == 'POST'):
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        messages.success(request, 'Updated : %s' % todo.title)
        todo.save()
        return redirect(reverse('todos:detail', args=[ id ]))
    else:
        context = {
            'todo':todo
        }
        return render(request, 'edit.html', context)

def delete(request, id):
    if (request.method == 'POST'):
        todo = get_object_or_404(Todo, pk=id)
        messages.success(request, 'Deleted : %s' % todo.title)
        todo.delete()

    return redirect(reverse('todos:index'))

