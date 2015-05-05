from django.conf.urls import patterns, url
from . import views
from django.views.generic import UpdateView


urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view()),
    url(r'^$', 'toDoTracker.views.index'), #name='index'),
    #url(r'^.*Edit-Task.html', views.EditTaskView.as_view()),
    url(r'^myobject/update/(?P<pk>\w+)?$', views.UpdateView.as_view(model=myModel, name='edit_task')),
    #url(r'^.*New-Task.html', views.NewTaskView.as_view()),
    url(r'^Impressum.html', views.ImpressumView.as_view()),
    url(r'^New-Task.html',
        'toDoTracker.views.newTask', name='newTask'),
    )

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#]
