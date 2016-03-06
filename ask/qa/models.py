from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = User()
    likes = models.ForeignKey(Likes, null=True, on_delete=models.SET_NULL)
    questtion = models.ForeignKey(Answer, null=True, on_delete=models.SET_NULL)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    author = User()

class Likes(models.Model):
    added_at = models.DateTimeField()
    author = User()
