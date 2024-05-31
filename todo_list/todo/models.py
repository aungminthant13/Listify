from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
        (4, 'No Priority'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=4, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['priority', 'complete', 'date', 'time']

