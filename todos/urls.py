from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='detail'),
    path('add', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('category', views.category_index, name='category/index'),
    path('category/add', views.category_add, name='category/add'),
    path('category/details/<int:category_id>', views.category_detail, name='category/details'),
    path('category/update/<int:category_id>', views.category_update, name='category/update'),
    path('category/delete/<int:category_id>', views.category_delete, name='category/delete'),
]

