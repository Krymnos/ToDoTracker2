from django.db import models
import datetime

class List(models.Model): 

  task = models.CharField(max_length=250)
  progress = models.IntegerField(default=0)
  deadline = models.DateField(default=datetime.datetime.now)
  completed = models.BooleanField(default=False)

  def __str__(self): 

    return self.task 

  class Meta: 

    ordering = ['task'] 

  class Admin: 

    pass

