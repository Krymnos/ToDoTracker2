from django.db import models
import datetime

class List(models.Model): 

  task = models.CharField(max_length=160)
  progress = models.IntegerField(default=0)
  deadline = models.CharField(max_length=20)
  completed = models.BooleanField(default=False)

  def __str__(self): 

    return self.task 

  class Meta: 

    ordering = ['task'] 

  class Admin: 

    pass
