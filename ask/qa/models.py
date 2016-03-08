from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from ask import settings

# Create your models here.
class Likes(models.Model):
    added_at = models.DateTimeField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    class META:
        db_table = 'likes'


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    likes = models.ForeignKey(Likes, null=True, on_delete=models.SET_NULL)

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

    class META:
        db_table = 'question'


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    class META:
        db_table = 'answer'
