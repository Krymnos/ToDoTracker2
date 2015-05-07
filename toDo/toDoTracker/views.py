from django.shortcuts import render
import sqlite3
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from django.views.generic.edit import DeleteView
from toDoTracker.models import List
from django.core.urlresolvers import reverse

#class IndexView(TemplateView):
#   template_name = 'ToDo-Tracker.html'

def index(request):
    conn = sqlite3.connect("db.sqlite3") 
    cursor = conn.cursor()
    cursor.execute("Select * from toDoTracker_list")
    conn.commit()
    rows = cursor.fetchall()
    context = {'rows': rows}
    return render(request, 'ToDo-Tracker.html', context)

class EditTaskView(TemplateView):
   template_name = 'Edit-Task.html'

class NewTaskView(TemplateView):
   template_name = 'New-Task.html'

class ImpressumView(TemplateView):
   template_name = 'Impressum.html'

class IndexView(TemplateView):
    template_name = 'ToDo-Tracker.html'

class IndexView(ListView):
    template_name = 'ToDo-Tracker.html'
    model = List

class ToDoCreate(CreateView):
    template_name = 'New-Task.html'
    model = List
    fields = ['task', 'progress', 'deadline']
    success_url ='/toDoTracker/'

class TaskUpdateView(UpdateView):
    template_name = 'Edit-Task.html'
    model = List
    fields = ['task', 'progress', 'deadline']
    succes_url = '/toDoTracker/'

class TaskDeleteView(DeleteView):
    template_name = 'Delete-Task.html'
    model = List
    succes_url = '/toDoTracker/'
