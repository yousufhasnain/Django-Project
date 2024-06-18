from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskList(models.Model):
    task=models.CharField(max_length=250)
    done=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return str(self.id) +" - "+ self.task +" - "+str(self.done)
    
    
    
