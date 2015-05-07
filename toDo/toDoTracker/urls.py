from django.conf.urls import patterns, url
from toDoTracker import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^edit/(?P<pk>\d+)$', views.TaskUpdateView.as_view(), name='edit_task'),
    url(r'^New-Task.html', views.ToDoCreate.as_view(), name = 'new_task'),
    url(r'^Impressum.html', views.ImpressumView.as_view()),
    url(r'^toDoTracker/(?P<pk>[0-9]+)/$', views.finishTask, name='finishTask')
    
    )
