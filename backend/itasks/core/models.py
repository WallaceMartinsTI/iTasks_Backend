from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    startDate = models.DateField()
    endDate = models.DateField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
