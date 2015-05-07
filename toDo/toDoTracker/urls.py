from django.conf.urls import patterns, url
from toDoTracker import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^edit/(?P<pk>\d+)$', views.TaskUpdateView.as_view(), name='edit_task'),
    url(r'^New-Task.html', views.ToDoCreate.as_view(), name = 'new_task'),
    url(r'^Impressum.html', views.ImpressumView.as_view()),
    url(r'^delete/(?P<pk>\d+)$', views.TaskDeleteView.as_view(), name='delete_task'),
    
    )
