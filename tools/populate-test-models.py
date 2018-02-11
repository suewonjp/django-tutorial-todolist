import os, sys, django

def add_test_todos():
    print('Populating Todo objects...')

    if not Todo.objects.filter(title='My 1st Todo'):
        todo = Todo(title='My 1st Todo', text='Reading...')
        todo.save()
    if not Todo.objects.filter(title='My 2nd Todo'):
        todo = Todo(title='My 2nd Todo', text='Playing with my dog...')
        todo.save()
    if not Todo.objects.filter(title='My 3rd Todo'):
        todo = Todo(title='My 3rd Todo', text='Eating...')
        todo.save()
    if not Todo.objects.filter(title='My 4th Todo'):
        todo = Todo(title='My 4th Todo', text='Sleeping...')
        todo.save()
    if not Todo.objects.filter(title='My 5th Todo'):
        todo = Todo(title='My 5th Todo', text='Debugging...')
        todo.save()

def add_test_categories():
    print('Populating Category objects...')

    if not Category.objects.filter(name='work'):
        category = Category(name='work')
        category.save()
    if not Category.objects.filter(name='life'):
        category = Category(name='life')
        category.save()
    if not Category.objects.filter(name='hobby'):
        category = Category(name='hobby')
        category.save()
    if not Category.objects.filter(name='study'):
        category = Category(name='study')
        category.save()

def add_relations():
    print('Populating relations between objects...')

    category = Category.objects.filter(name='work').get()
    if not category.todos.all():
        category.todos.add(Todo.objects.filter(title='My 5th Todo').get())

    category = Category.objects.filter(name='life').get()
    if not category.todos.all():
        category.todos.add(Todo.objects.filter(title='My 3rd Todo').get())
        category.todos.add(Todo.objects.filter(title='My 4th Todo').get())

    category = Category.objects.filter(name='hobby').get()
    if not category.todos.all():
        category.todos.add(Todo.objects.filter(title='My 1st Todo').get())
        category.todos.add(Todo.objects.filter(title='My 2nd Todo').get())

    category = Category.objects.filter(name='study').get()
    if not category.todos.all():
        category.todos.add(Todo.objects.filter(title='My 1st Todo').get())

if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.curdir))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todolist.settings")
    django.setup()

    from todos.models import Todo
    from todos.models import Category

    if Todo.objects.all():
        print('You have data in the db.')
        print('Executing this script may mess with the existing data.')
        print('Still want to proceed? (y/n)')
        y = input().lower()
        if y != 'y' and y != 'yes':
            print('Aborting...')
            sys.exit()

    add_test_todos()
    add_test_categories()
    add_relations()

