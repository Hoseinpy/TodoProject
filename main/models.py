from django.db import models
from django.contrib.auth.models import User


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name