from django.shortcuts import render
import sqlite3
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from toDoTracker.models import List

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



def newTask(request):
    if request.method == 'GET':
        form = NewTaskForm()
    else:
        # A POST request: Handle Form Upload
        form = NewTaskForm(request.POST) # Bind data from request.POST into a NewTaskForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            task = form.cleaned_data['task']
            progress = str(form.cleaned_data['progress'])
            deadline = str(form.cleaned_data['deadline'])
            
 
            conn = sqlite3.connect("db.sqlite3") 
            cursor = conn.cursor()
            cursor.execute("INSERT INTO toDoTracker_list VALUES (null,'"+task+"', "+progress+", 'false', '"+deadline+"')")
            conn.commit()
 
    return render(request, 'New-Task.html', {
        'form': form,
    })


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
