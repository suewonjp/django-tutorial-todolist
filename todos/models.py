from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s: %s' % (self.id, self.title)

class Category(models.Model):
    name = models.CharField(max_length=50)
    todos = models.ManyToManyField(Todo)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

