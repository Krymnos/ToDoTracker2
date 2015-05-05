from django import forms
 
class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=160)
    progress = forms.IntegerField()
    deadline = forms.DateTimeField()
