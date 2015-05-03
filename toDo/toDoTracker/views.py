from django.views.generic import TemplateView

class IndexView(TemplateView):
   template_name = 'ToDo-Tracker.html'

class EditTaskView(TemplateView):
   template_name = 'Edit-Task.html'

class NewTaskView(TemplateView):
   template_name = 'New-Task.html'

class ImpressumView(TemplateView):
   template_name = 'Impressum.html'

#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#    template = loader.get_template('ToDo-Tracker.html')
#    return HttpResponse(template)
