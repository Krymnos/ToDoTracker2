from django.conf.urls import patterns, url
from . import views
from django.views.generic.edit import UpdateView
from toDoTracker.models import List


urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view()),
    url(r'^$', 'toDoTracker.views.index'), #name='index'),
    url(r'^Edit-Task.html', views.EditTaskView.as_view()),
    #url('^to_do_update/(?P<pk>[\w-]+)$', views.EditTaskView.as_view()),
    #url(r'^.*New-Task.html', views.NewTaskView.as_view()),
    url(r'^Impressum.html', views.ImpressumView.as_view()),
    url(r'^New-Task.html',
        'toDoTracker.views.newTask', name='newTask'),
    )

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#]
