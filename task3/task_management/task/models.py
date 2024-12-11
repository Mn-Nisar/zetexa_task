from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title