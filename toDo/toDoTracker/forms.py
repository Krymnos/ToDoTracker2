from django import forms
from toDoTracker.models import List
 
class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=160)
    progress = forms.IntegerField()
    deadline = forms.DateTimeField()

class EditTaskForm(forms.Form):
    task = forms.CharField(max_length=160)
    progress = forms.IntegerField()
    deadline = forms.DateTimeField()

