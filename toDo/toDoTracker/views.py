from django.views.generic import TemplateView
from django.shortcuts import render
from toDoTracker.forms import NewTaskForm
import sqlite3
from django.views.generic.edit import UpdateView
from toDoTracker.models import List
from django.http import HttpResponseRedirect

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

#class ToDoUpdateView(UpdateView):
    #model = List
    #fields = ['task']
    #fields = ['progress']
    #fields = ['deadline']
    #fields = ['completed']
    #template_name = 'Edit-Task.html'

    def toDoUpdate(request, object_id):

        toDo = get_object_or_404(List, pk=object_id)
        info_send = False

        if request.method == "POST":
            form = editTaskForm(request.POST, request.FILES, instance=toDo)

            if form.is_valid():
                cd = form.cleaned_data
                task = cd.get('task') #user get() instead of []
                progress = form.cleaned_data['progress']
                deadline = form.cleaned_data['deadline']
                completed = form.cleaned_data['completed']

                toDo.task = cd.get('task') #user get() instead of []
                toDo.progress = progress
                toDo.deadline = deadline
                toDo.completed = completed
                toDo.save()

                info = "Updated"
                info_send = True

                return HttpResponseRedirect('/')
            else:
                #print form.errors
                info = "ERROR updating"

        else:
            form = editProductForm(instance=tpoDo)
            ctx = {'form':form}
        return render_to_response('Edit-Task.html', ctx, context_instance=RequestContext(request))


#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#    template = loader.get_template('ToDo-Tracker.html')
#    return HttpResponse(template)
