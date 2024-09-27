from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
