from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Connect Task to specific user
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title # Try f"{self.title}"