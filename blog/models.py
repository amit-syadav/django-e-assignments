from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Assignment(models.Model):
    #assign = models.ForeignKey(Post, on_delete=models.CASCADE)
    # quest = models.TextField(null = True)
    # q_author = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.TextField(null = True)
    # content = models.TextField(null = True)
    # id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
