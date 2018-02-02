from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='detail'),
    path('add', views.add, name='add')
]

