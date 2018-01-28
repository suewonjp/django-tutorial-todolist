from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^details/(?P<id>\w{0,50})/$', views.details),
    # re_path(r'^add', views.add, name='add')
]

