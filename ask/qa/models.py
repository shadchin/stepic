from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    author = User()
    class META:
        db_table = 'answer'


class Likes(models.Model):
    added_at = models.DateTimeField()
    author = User()
    class META:
        db_table = 'likes'


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = User()
    likes = models.ForeignKey(Likes, null=True, on_delete=models.SET_NULL)
    questtion = models.ForeignKey(Answer, null=True, on_delete=models.SET_NULL)
    class META:
        db_table = 'question'
