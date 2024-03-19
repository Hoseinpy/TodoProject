from django.db import models


class TodoModel(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name