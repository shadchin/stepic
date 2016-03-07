from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Likes(models.Model):
    added_at = models.DateTimeField()
    author = User()
    class META:
        db_table = 'likes'


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField(null=True)
    author = User()
    likes = models.ForeignKey(Likes, null=True, on_delete=models.SET_NULL)

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

    class META:
        db_table = 'question'


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    author = User()
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    class META:
        db_table = 'answer'
