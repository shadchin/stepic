from django.forms import ModelForm, Form, CharField, EmailField, PasswordInput
from django.contrib.auth.models import User

from qa.models import Question, Answer

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']


class SignupForm(Form):
    username = CharField()
    email = EmailField()
    password =  CharField(widget=PasswordInput())

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginForm(Form):
    username = CharField()
    password =  CharField(widget=PasswordInput())
