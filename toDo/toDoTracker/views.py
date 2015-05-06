from django.views.generic import TemplateView
from django.shortcuts import render
from toDoTracker.forms import NewTaskForm
import sqlite3
from django.views.generic.edit import UpdateView
from toDoTracker.models import List
#from django.http import HttpResponseRedirect

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

class ToDoUpdate(UpdateView):
    model = List
    fields = ['task']
    fields = ['progress']
    fields = ['deadline']
    fields = ['completed']
    template_name = 'Edit-Task.html'



#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#    template = loader.get_template('ToDo-Tracker.html')
#    return HttpResponse(template)
