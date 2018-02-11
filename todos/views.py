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
        messages.success(request, 'Added : %s' % todo.title)
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
        categories = request.POST.getlist('category-select')
        todo.category_set.clear()
        if categories:
            for cid in categories:
                category = Category.objects.get(id=cid)
                todo.category_set.add(category)
        todo.save()
        messages.success(request, 'Updated : %s' % todo.title)
        return redirect(reverse('todos:detail', args=[ id ]))
    else:
        attached_categories = todo.category_set.all()
        categories = [(True,c) if attached_categories.filter(id=c.id) else (False, c) for c in Category.objects.all() ]

        context = {
            'todo':todo,
            'categories':categories
        }
        return render(request, 'edit.html', context)

def delete(request, id):
    if (request.method == 'POST'):
        todo = get_object_or_404(Todo, pk=id)
        messages.success(request, 'Deleted : %s' % todo.title)
        todo.delete()

    return redirect(reverse('todos:index'))

def category_index(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'category/index.html', context)

def category_add(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        category = Category(name=name)
        category.save()
        messages.success(request, 'Category Added : %s' % category.name)
        return redirect(reverse('todos:index'))
    else:
        categories = Category.objects.all()
        context = {
            'categories':categories
        }
        return render(request, 'category/add.html', context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
            'category':category,
            'todos':category.todos.all()
    }
    return render(request, 'category/detail.html', context)

def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if (request.method == 'POST'):
        category.name = request.POST['name']
        category.save()
        messages.success(request, 'Category Updated : %s' % category.name)
        return redirect(reverse('todos:category/detail', args=[ category_id ]))
    else:
        categories = Category.objects.all()
        context = {
            'categories':categories,
            'category':category
        }
        return render(request, 'category/edit.html', context)


def category_delete(request, category_id):
    if (request.method == 'POST'):
        category = get_object_or_404(Category, pk=category_id)
        messages.success(request, 'Category Deleted : %s' % category.name)
        category.delete()

    return redirect(reverse('todos:index'))

